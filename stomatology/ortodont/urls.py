from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/<str:slug>/', about, name='about'),
    path('contact/<str:slug>/', contact, name='contact'),
    path('services/<str:slug>/', services, name='services'),
]