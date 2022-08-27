from django.shortcuts import redirect, render

from store.models import customers
from ..models.product import Product
from ..models.orders import Order
from django.views import View
from store.midleware.auth import authMiddleware
from django.utils.decorators import method_decorator
class OrderView(View):
    @method_decorator(authMiddleware)
    def get(self, request):
        customer=request.session.get('customer')
        orders=Order.getOrderByCustomer(customer)
        return render(request, 'order.html',{'orders':orders})

  
