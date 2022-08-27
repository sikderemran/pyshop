from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from .product import Product
from .customers import Customer
import datetime

from store.models import customers

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.CharField(max_length=255,default='',blank=True)
    address=models.CharField(max_length=255,default='',blank=True)
    mobile=models.CharField(max_length=255,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    



    def placeOrder(self):
        self.save()

    @staticmethod
    def getOrderByCustomer(customer_id):
        return Order.objects.filter(customer=customer_id)