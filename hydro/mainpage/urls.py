from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('faculty', faculty, name='faculty'),
    path('about_conference', about_conference, name='about_conference'),
    path('contacts', contacts, name='contacts'),
    path('download_thesis', download_theses, name='download_theses'),
    ]