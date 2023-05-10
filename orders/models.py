from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import Products 
from products.models import Offers, Products


class BillingInfo(models.Model):
    """
    A model to store billing information for an order.
    """
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    house_nr = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)


class PaymentInfo(models.Model):
    """
    A model to store payment information for an order.
    """
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)



class UserOrder(models.Model):
    """
    A model to store the user's order information.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, user, order_id, product_id=None, offer_id=None):
        if product_id:
            product = Products.objects.get(id=product_id)
        else:
            product = None
        if offer_id:
            offer = Offers.objects.get(id=offer_id)
        else:
            offer = None
        return cls(user=user, product=product, offer=offer, order_id=order_id)

    def get_product_or_offer_name(self):
            if self.product:
                return self.product.name
            elif self.offer:
                return self.offer.name
            else:
                return 'Unknown'

