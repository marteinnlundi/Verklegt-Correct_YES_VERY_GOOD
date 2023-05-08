from django.db import models
from django.contrib.auth.models import User 


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='product_images', max_length=999)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Offers(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    images = models.ImageField(upload_to='offer_images', max_length=999)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name



