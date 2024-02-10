from django.contrib import admin
from .models.product import Products
from .models.category import Category, SubCategory
from .models.customer import CustomUser
from .models.orders import Order
from .models.productpage import ProductImages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "profile_pic", "phone", "username", "is_active", "is_staff"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["phone"]}),
        ("Permissions", {"fields": ["is_ative"]}),
    ]
    list_filter = ["email", "is_staff", "is_active"]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "phone", "profile_pic", "username", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions",],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]

   
    
class AdminProductImages(admin.ModelAdmin):
    model = ProductImages


class AdminProduct(admin.ModelAdmin):
        fields = ['name', 'price', 'description','image', 'category', 'subcategory']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Order)
admin.site.register(ProductImages)
admin.site.register(SubCategory)

