from django.shortcuts import render , redirect , HttpResponseRedirect
from pooltables.models.product import Products
from pooltables.models.category import Category, SubCategory
from django.views import View


# Create your views here
class store(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('pooltables')
    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/pooltables{request.get_full_path()[1:]}')



def pooltables(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    subcategories = SubCategory.get_all_subcategories()
    subcategory_id = request.GET.get('subcategory')
    category_id = request.GET.get('category')
    if category_id:
        if subcategory_id:
            products = Products.get_all_products_by_subcategoryid(subcategory_id)
        else:
            products = Products.get_all_products_by_categoryid(category_id)
    else:
            products = Products.get_all_products()
            
    data = {
    'products': products,
    'categories': categories,
    'subcategories': subcategories,
    'selected_category_id': int(category_id) if category_id else None,
    'selected_subcategory_id': int(subcategory_id) if subcategory_id else None,
    }


    print('you are : ', request.session.get('email'))
    return render(request, 'shop.html', data)

