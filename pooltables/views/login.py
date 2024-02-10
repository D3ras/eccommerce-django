from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from django.views import View

class Login(View):

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        user = authenticate(email=email, password=password)
        error_message = None
        if user is not None:
            flag = check_password (password, user.password)
            if flag:
                request.session['user'] = user.id

                if Login.return_url:
                    return Response(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid login credentials!!'
        else:
            error_message = 'Invalid login credentials !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')

