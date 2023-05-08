from django.db import models
from django import forms

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='user_images')
    email = models.EmailField()
    password = models.CharField(max_length=100)



