# FIRSTAPPLICATION/models.py
from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'FIRSTAPPLICATION'

class ID(models.Model):
    identifier = models.CharField(max_length=20)

    class Meta:
        app_label = 'FIRSTAPPLICATION'

class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        app_label = 'FIRSTAPPLICATION'

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        app_label = 'FIRSTAPPLICATION'
