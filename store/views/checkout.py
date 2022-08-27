from statistics import quantiles
from django.shortcuts import redirect, render

from ..models.customers import Customer
from ..models.product import Product
from ..models.orders import Order
from django.views import View

class Checkout(View):
    def post(self, request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.getCartProduct(list(cart.keys()))
        print(products)
        for product in products:
            order=Order(
                    product=product,
                    customer=Customer(id=customer),
                    quantity=cart.get(str(product.id)),
                    address=address,
                    price=product.price,
                    mobile=phone
                )
            order.placeOrder()
        request.session['cart']={}
        return redirect('cart')
      

  
