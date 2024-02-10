from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DetailView
from pooltables.models.product import Products
from pooltables.models.productpage import ProductImages


class ProductDetailView(DetailView):
    model = Products
    template_name = 'detail.html'
    context_object_name = 'product'
    
    def post(self, request, *args, **kwargs):
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
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    def get_context_data(self, **kwargs):
        cart = self.request.session.get('cart')
        context = super().get_context_data(**kwargs)
        product = context[self.context_object_name]
        images = ProductImages.objects.filter(product=product)
        context['images'] = images
        context['cart'] = cart 
        return context
    
    


