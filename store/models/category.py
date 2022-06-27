import imp
from django.db import models
from django.forms import CharField

class Category(models.Model):
    name = models.CharField(max_length=100, default='')

    @staticmethod
    def getAllCategories():
        return Category.objects.all()

    def __str__(self):
        return self.name
