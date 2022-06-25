from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product

def index(request):
    #return HttpResponse('<h1>Hello</h1>')
    products=Product.getAllProducts()
    return render(request,'index.html',{'products':products})
