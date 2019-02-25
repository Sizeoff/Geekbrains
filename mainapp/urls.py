from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [

    path('katalog/', mainapp.katalog, name = 'katalog'),
    path('contacts/', mainapp.contacts, name = 'contacts'),
    path('', mainapp.main, name = 'main'),
]