from django.shortcuts import render , redirect , HttpResponseRedirect
from pooltables.models.product import Products
from pooltables.models.category import Category
from django.views import View


# Create your views here
class Index(View):
   def home(request):

    return  HttpResponseRedirect('index.html')

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/pooltables{request.get_full_path()[1:]}')

