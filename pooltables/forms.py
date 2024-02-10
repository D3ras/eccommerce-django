from django import forms
from pooltables.models.product import Products
from pooltables.models.customer import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models.category import Category, SubCategory
from django.contrib.auth.forms import UserCreationForm

class ProductsSearchForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'image']

class UserCreationForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    profile_pic = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': False}))
    class Meta:
        model = CustomUser
        fields = ['phone', 'email', 'username', 'profile_pic', 'password1', 'password2']
     

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.cleaned_data.get("profile_pic"):
            user.profile_pic = self.cleaned_data["profile_pic"]

        if commit:
            user.save()

        return user
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ["email",]
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "phone"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["phone"]}),
        ("Permissions", {"fields": ["is_ative"]}),
    ]
    list_filter = ["is_active"]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "phone", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]

#   class Meta:
#       model = Products
#        fields = '__all__'
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#       if 'category' in self.fields and 'subcategory' in self.fields:
#            # Filter categories based on the selected subcategory
#            subcategory_field = self.fields['subcategory']
#            category_field = self.fields['category']
#            subcategory_field.widget.attrs['onchange'] = 'filter_categories(this.value);'
#            self.filter_categories(None)  # Initial load without subcategory selection
#
#    def filter_categories(self, subcategory_id):
#        try:
#            if subcategory_id:
#                # Get the selected subcategory
#                subcategory = SubCategory.objects.get(id=subcategory_id)
#                
#                # Filter categories based on the selected subcategory's associated category
#                self.fields['category'].queryset = Category.objects.filter(id=subcategory.category.id)
#            else:
#                # If no subcategory is selected, display all categories
#                self.fields['category'].queryset = Category.objects.all()
#        except SubCategory.DoesNotExist:
#            # Handle the case where subcategory_id is None or invalid
#            self.fields['category'].queryset = Category.objects.none()
