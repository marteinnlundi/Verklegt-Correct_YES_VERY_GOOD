from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='user_images')
    email = models.EmailField()
    password = models.CharField(max_length=100)


