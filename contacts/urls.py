from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_page, name="contact"),       # renders your contact.html
    path("send/", views.contact_api, name="contact_api"),  # handles POST (AJAX/JSON)
]
