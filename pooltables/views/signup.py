from django.shortcuts import render , redirect , HttpResponseRedirect
from rest_framework import status
from rest_framework import permissions
from django.views import View
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from django.contrib import messages
from pooltables.tokens import email_auth_otp
from pooltables.serializers import (CreateUserSerializer,
                              MyProfileSerializer,
                              UploadUserPicSerializer)
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from pooltables.models.customer import CustomUser
from pooltables.forms import UserCreationForm

class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST, request.FILES)
        error = None 
        
        if form.is_valid():
        
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            profile_pic = form.cleaned_data['profile_pic']
        

            error = self.validateCustomUser(username, phone, email, password1, password2)

            if not error:
                user = form.save(commit=False)
                password1 = form.cleaned_data['password1']
                user.set_password(password1)
                user.save ()
                return redirect ('login')
            else:
                messages.error(request, error)
        else:
             messages.error(request, 'Please correct errors below')
        return render (request, 'signup.html', {'form': form})
        
    def validateCustomUser(self, username, phone, email, password1, password2):
        # Form Validations
        error = None
        if not username:
            error = 'Please Enter your User name'
        elif len (username) < 3:
            error_message = 'User Name must be 3 char long or more'
        elif not phone:
            error = 'Enter your Phone Number'
        elif len (phone) < 10:
            error = 'Phone Number must be 10 char Long'
        elif len (password1) or len (password2) < 5:
            error = 'Password must be 5 char long'
        elif password1 != password2:
            error = 'passwords do not match'
        elif len (email) < 5:
            error = 'Email must be 5 char or more long'
        elif CustomUser.objects.filter(email=email).exists():
            error = 'Email Address Already Registered'




        return error

     

