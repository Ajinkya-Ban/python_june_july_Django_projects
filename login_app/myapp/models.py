from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django import forms
# Create your models here.

class LoginForm(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username