from django.db import models
from .product import Products
from .category import Category

class  ProductImages(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,default=1 )
    images = models.FileField(upload_to='uploads/products/')

    def __str__(self):
        return self.product.name
