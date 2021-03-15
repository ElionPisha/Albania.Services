from django.db import models

# Create your models here.

class Home(models.Model):
    images = models.ImageField(upload_to='media/')
    tittle = models.CharField(max_length=100)
    Url = models.URLField(max_length=500)

    def __str__(self):
        return self.tittle

class Partneret(models.Model):
    images = models.ImageField(upload_to='media/')

class Projektet(models.Model):
    images = models.ImageField(upload_to='media/')
    tittle = models.CharField(max_length=80)

    def __str__(self):
        return self.tittle

class Rrethnesh(models.Model):
    text = models.TextField(max_length=10000)
    text1 = models.TextField(max_length=10000)
    images = models.ImageField(upload_to='media/')

class Kontakt(models.Model):
    tittle = models.CharField(max_length=30)
    text = models.TextField(max_length=6000)
    adresa = models.CharField(max_length=60)
    cel = models.CharField(max_length=20)
    cel1 = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    map = models.URLField(max_length=1000)

    def __str__(self):
        return self.tittle

class Sherbimet(models.Model):
    tittle = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    list1 = models.CharField(max_length=500)
    list2 = models.CharField(max_length=500)
    list3 = models.CharField(max_length=500)
    list4 = models.CharField(max_length=500)
    list5 = models.CharField(max_length=500)
    list6 = models.CharField(max_length=500)
    list7 = models.CharField(max_length=500)
    list8 = models.CharField(max_length=500)
    list9 = models.CharField(max_length=500)
    list10 = models.CharField(max_length=500)
    list11 = models.CharField(max_length=500)
    list12 = models.CharField(max_length=500)
    list13 = models.CharField(max_length=500)
    list14 = models.CharField(max_length=500)
    list15 = models.CharField(max_length=500)
    images = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.tittle
