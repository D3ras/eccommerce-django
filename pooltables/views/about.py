from django.views import View
from django.shortcuts import render , redirect , HttpResponseRedirect

class About(View):
   def get(self, request):

    return  render(request, 'hom.html')

