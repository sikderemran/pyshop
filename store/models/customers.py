from django.db import models


class Customer(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=500)


