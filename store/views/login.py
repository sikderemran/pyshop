from tkinter.messagebox import NO
from django.shortcuts import redirect, render,HttpResponseRedirect
from ..forms.form import CustomerForm
from django.views import View

class Login(View):
    returnUrl=None
    def get(self, request):
        Login.returnUrl=request.GET.get('returnUrl')
        form = CustomerForm()
        data = {'form': form}
        return render(request, 'login.html', data)

    def post(self, request):
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            customer = form.login()
        if customer:
            request.session['customer']=customer.id
            if Login.returnUrl:
                return HttpResponseRedirect(Login.returnUrl)
            else:
                Login.returnUrl=None
                return redirect('homepage')
        else:
            error = '''Email or Password Incorrect'''
            data = {'form': form, 'error': error}
            return render(request, 'login.html', data)

def logout(request):
    request.session.clear()
    return redirect('login')
