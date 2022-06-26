from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product
from .models.product import Category


def index(request):
    # return HttpResponse('<h1>Hello</h1>')
    products = None
    categories = Category.getAllCategories()
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.getProductById(categoryId)
    else:
        products = Product.getAllProducts()
    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)


def signup(request):
    return render(request, 'signup.html')