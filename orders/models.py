from django.db import models 

from django.contrib.auth.models import User
#from django.contrib.auth.models import Products 
from products.models import Products
class BillingInfo(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    house_nr = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

class PaymentInfo(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)

class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)

