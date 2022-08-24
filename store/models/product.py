from distutils.command.upload import upload
from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='upload/products/')
    category = models.ForeignKey(Category, models.CASCADE)

    @staticmethod
    def getAllProducts():
        return Product.objects.all()

    @staticmethod
    def getProductById(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()
    
    @staticmethod
    def getCartProduct(ids):
        return Product.objects.filter(id__in=ids)
