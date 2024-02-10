from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from pooltables.models.customer import CustomUser
from django.views import View

from pooltables.models.product import Products
from pooltables.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.session.get('user')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customuser, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(user=CustomUser(id=user),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
