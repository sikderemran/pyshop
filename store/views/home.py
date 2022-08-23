from django.shortcuts import redirect, render
from django.views import View
from ..models.product import Product
from ..models.product import Category
from ..forms.form import CustomerForm

class Index(View):
    def get(self,request):
        products = None
        cart=request.session.get('cart')
        if not cart:
           request.session['cart']={}
        categories = Category.getAllCategories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.getProductById(categoryId)
        else:
            products = Product.getAllProducts()
        data = {'products': products, 'categories': categories}
        return render(request, 'index.html', data)
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity<=1:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        return redirect('homepage')

    



