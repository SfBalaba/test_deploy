from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import forms
from django.contrib.auth.models import AbstractUser

class Home_data(models.Model):
    title = models.CharField(max_length=50, )
    file = models.ImageField(upload_to="images")
    excel = models.FileField(upload_to="excel")
    html = models.TextField(default="")

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=50, )
    file = models.ImageField(upload_to="images")
    html = models.TextField(default="")

    def __str__(self):
        return self.title




class Buyer(AbstractUser):
    ...


