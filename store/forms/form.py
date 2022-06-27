from django import forms
from ..models.category import Category

class UserForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control form-control-sm',
                'placeholder':'name'
                })
        }
