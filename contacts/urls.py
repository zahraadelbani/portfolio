# urls.py (your app or project)
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_page, name='contact'),
    path('contact/send/', views.contact_api, name='contact_api'),
]
