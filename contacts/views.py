# views.py
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from django.conf import settings

from .forms import ContactForm

def contact_page(request):
    # Renders your existing template (GET only)
    return render(request, 'contacts/contact.html')  # adjust template name/path if different

@require_POST
@csrf_protect
def contact_api(request):
    """
    Accepts JSON (or form-encoded) POSTs and returns JSON response.
    Expects X-CSRFToken header (we'll add that from the frontend).
    """
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except ValueError:
        # if not JSON, fallback to request.POST
        payload = request.POST

    form = ContactForm(payload)
    if not form.is_valid():
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    data = form.cleaned_data

    # Prepare email
    subject = f"Website contact from {data['name']}"
    message = f"Name: {data['name']}\nEmail: {data['email']}\n\nMessage:\n{data['message']}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient = getattr(settings, "DEFAULT_TO_EMAIL", settings.DEFAULT_FROM_EMAIL)

    if recipient:
        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=[recipient],
                headers={'Reply-To': data['email']}  # user email for reply
            )
            email.send(fail_silently=False)
        except Exception as e:
            # Log error in production
            return JsonResponse({'success': False, 'error': 'Failed to send email.'}, status=500)

    # Option B: (optional) save to DB
    # ContactMessage.objects.create(**data)

    return JsonResponse({'success': True})
