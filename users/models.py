from django.db import models
from django import forms


import users

class Profile(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='user_images')
    email = models.EmailField()
    password = models.CharField(max_length=100)


from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if users.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match')