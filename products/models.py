from django.db import models



class Products(models.Model):
    """
    A single product
    
    Attributes:
    name (str): The name of the product.
    description (str): The description of the product.
    images (ImageField): The image of the product.
    price (int): The price of the product.
    type (str): The type of the product.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='product_images', max_length=999)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Offers(models.Model):
    """
    A single offer
    
    Attributes:
    name (str): The name of the offer.
    description (str): The description of the offer.
    images (ImageField): The image of the offer.
    price (int): The price of the offer.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    images = models.ImageField(upload_to='offer_images', max_length=999)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.name



