# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(max_length=254, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), max_length=2000, required=True)

    def clean_message(self):
        msg = self.cleaned_data['message']
        # optional: additional validation
        return msg
