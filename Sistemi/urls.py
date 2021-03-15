from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sherbimet.html', views.sherbimet, name='sherbimet'),
    path('projektet.html', views.projektet, name='projektet'),
    path('rrethnesh.html', views.rrethnesh, name='rrethnesh'),
    path('kontakt.html', views.kontakt, name='kontakt'),


]