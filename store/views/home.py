from django.shortcuts import redirect, render
from ..models.product import Product
from ..models.product import Category
from ..forms.form import CustomerForm

def index(request):
    # return HttpResponse('<h1>Hello</h1>')
    #print(request.session.get('email'))
    products = None
    categories = Category.getAllCategories()
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.getProductById(categoryId)
    else:
        products = Product.getAllProducts()
    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)



