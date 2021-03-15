from django.shortcuts import render

# Create your views here.
from .models import Home, Partneret, Projektet, Rrethnesh, Kontakt, Sherbimet


def home(request):
    sherbimet = Home.objects.all()
    partner = Partneret.objects.all()
    return render(request, 'home.html', {'sherbimet': sherbimet, 'partner': partner})


def sherbimet(request):
    klient = Sherbimet.objects.all()
    return render(request, 'sherbimet.html', {'klient': klient})


def projektet(request):
    projekte = Projektet.objects.all()
    return render(request, 'projektet.html', {'projekte': projekte})


def rrethnesh(request):
    nesh = Rrethnesh.objects.all()
    return render(request, 'rrethnesh.html', {'nesh': nesh})


def kontakt(request):
    kontakt = Kontakt.objects.all()
    return render(request, 'kontakt.html', {'kontakt': kontakt})


