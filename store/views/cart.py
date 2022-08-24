from django.shortcuts import redirect, render
from ..models.product import Product
from django.views import View

class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())
        Product.getCartProduct(ids)
        return render(request, 'cart.html')

  
