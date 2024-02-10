from django.shortcuts import render, redirect , HttpResponseRedirect,  get_object_or_404
from django.views import View
from django.contrib.auth.hashers import check_password
from pooltables.models.customer import CustomUser
from django.utils.decorators import method_decorator
from django.contrib import messages
from pooltables.middlewares.auth import auth_middleware
from django.contrib import messages

class Profile(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            user_email = request.user.email
            customuser = CustomUser.objects.filter(email=user_email).first()
            if customuser:
                profile = get_object_or_404(user=customuser)
                details = {
                    'customuser':customuser,
                    'profile':profile,
                    }
                return render(request, 'updateprofile.html', details)

            else:
                # Handle the case where the CustomUser does not exist
                messages.warning(request, "CustomUser not found.")
                return HttpResponseRedirect('login')

        else:
            # Handle the case where the user is not authenticated
            messages.warning(request, "You need to be logged in.")
            return HttpResponseRedirect('login')

    def post(self, request):
        user = request.user
        customuser = CustomUser.objects.filter(email=user.email)

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        image = request.FILES.get('avatar.jpg')

        # Form Validations
        if len(fname) > 10 or len(lname) > 10:
            messages.warning(request, "First or Last Name too long!!!")
            return HttpResponseRedirect('profile')

        if not fname.isalpha() or not lname.isalpha():
            messages.warning(request, "Name must contain only letters.")
            return HttpResponseRedirect('profile')

        if len(str(phone)) != 10:
            messages.warning(request, "Phone number must contain 10 digits.")
            return HttpResponseRedirect('profile')

        # Update the CustomUser fields
        customuser.phone = phone
        customuser.email = email
        customuser.first_name = fname
        customuser.last_name = lname
        customuser.username = username
        customuser.profile_pic = image
        customuser.save()


        messages.success(request, "Your Account has been successfully updated!!!")
        return redirect('account')
