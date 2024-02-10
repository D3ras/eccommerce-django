from django.contrib import admin
from django.urls import path
from .views.home import pooltables, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.search import search
from . import views
from .views.product import ProductDetailView
from .views.about import About
from .views.gallery import photos_gallery
from .views.profile import Profile
from .middlewares.auth import  auth_middleware
from .views.account import account

urlpatterns = [
    path('', About.as_view(), name='homepage'),
    path('store', store.as_view(), name='store'),
    path('pooltables/', pooltables, name='pooltables'),
    path('search', search, name='search'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', auth_middleware(CheckOut.as_view()), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail_view'),
    path('photos/', photos_gallery, name='photos'),
    path('profile', auth_middleware(Profile.as_view()), name='profile'),
    path('account', account, name='account'),
]
