from django.db import models
from .product import Products
from .customer import CustomUser
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customuser = models.ForeignKey(CustomUser,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customuser(customuser_id):
        return Order.objects.filter(customuser=customuser_id).order_by('-date')
