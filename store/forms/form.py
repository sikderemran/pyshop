from django import forms
from ..models.customers import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        widgets={
            'firstName':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'first name'
                }),
            'lastName':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'Last name'
                }),
            'phone':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'Phone'
                }),
            'email':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'Email'
                }),
            'password':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'Password'
                })
        }
    def register(self):
        #self.data['email']
        self.save()
    
