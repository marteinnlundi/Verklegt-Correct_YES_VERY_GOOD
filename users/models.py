from django.db import models
from django import forms

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='user_images')
    email = models.EmailField()
    password = models.CharField(max_length=100)



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        fields = ['name', 'img', 'email', 'password']


 