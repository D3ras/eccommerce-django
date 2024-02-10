from pooltables.models.customer import CustomUser
from django.shortcuts import render
from django.utils.decorators import method_decorator
from pooltables.middlewares.auth import auth_middleware

def account(request):
    currentuser = request.user
    customuser = CustomUser.objects.get(id=currentuser.id)

    details = {
        'customuser':customuser,
        }

    return render(request, 'account.html', details)
