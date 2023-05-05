from django.db import models
from django.contrib.auth.models import User 


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='product_images')
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Offer(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
