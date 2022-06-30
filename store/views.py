from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models.product import Product
from .models.product import Category
from .forms.form import CustomerForm
from django.contrib.auth.hashers import make_password

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
    if request.method == 'POST':
        #print(request.POST.get('email'))
        form = CustomerForm(request.POST)
        #make_password(form.data['email'])
        if form.is_valid():
            try:
                form.register()
                # return HttpResponse("data send to database")
                return redirect('homepage')
            except:
                pass
    else:
        form = CustomerForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
    else:
        form = CustomerForm()
    return render(request, 'login.html', {'form': form})
