from django.db import models
from django import forms
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This class is used to create a user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='user_images')
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=100)



