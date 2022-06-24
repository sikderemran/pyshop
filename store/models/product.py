from distutils.command.upload import upload
from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255,default='')
    image = models.ImageField(upload_to='upload/products/')
    category=models.ForeignKey(Category,models.CASCADE)
    