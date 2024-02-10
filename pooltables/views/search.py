from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, reverse
from pooltables.models.product import Products
from pooltables.models.category import Category, SubCategory
from django.db.models import Q
from django.template import RequestContext


def search(request):
  query = request.GET.get('q')
  categories = Category.objects.all()
  subcategories = SubCategory.objects.all()
  if not query:
    return redirect('pooltables:homepage')

  # search in title, description, or features
  products = Products.objects.filter(category__name__icontains=query) | Products.objects.filter(name__icontains=query) | Products.objects.filter(description__icontains=query)

  return render(request, 'search_results.html', {
    'products': products,
    'name': 'Search Results',
    'categories': categories,
    'subcategories': subcategories
  })
