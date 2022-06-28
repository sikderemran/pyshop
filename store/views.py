from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product
from .models.product import Category
from .forms.form import CustomerForm

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
    if request.method=='POST':
        #print(request.POST.get('email'))
        customer=CustomerForm(request.POST)
        if customer.is_valid:
            try:
                customer.save()
                return HttpResponse("data send to database")
            except:
                pass
    form=CustomerForm()
    return render(request, 'signup.html',{'form':form})