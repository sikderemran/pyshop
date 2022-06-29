from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customers import Customer
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
