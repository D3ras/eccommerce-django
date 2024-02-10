from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from pooltables.models.customer import CustomUser
from django.views import  View
from pooltables.models.product import Products
from django.conf import settings
import requests
from pooltables.views.login import Login

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

def checkout(request):
    # Generate payment URL using Daraja API
    # You need to implement this logic based on your order details and Daraja API documentation
    # Example: https://developer.safaricom.co.ke/lipa-na-m-pesa-online/apis/post/safaricom-sandbox
    payment_url = "GENERATED_PAYMENT_URL"
    
    return render(request, 'checkout.html', {'payment_url': payment_url})
