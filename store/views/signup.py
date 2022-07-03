from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..forms.form import CustomerForm
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        # make_password(form.data['email'])
        if form.is_valid():
            try:
                form.register()
                # return HttpResponse("data send to database")
                return redirect('homepage')
            except:
                pass
        return render(request, 'signup.html', {'form': form})
