from atexit import register
from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "৳" + str(number)

@register.filter(name='priceMultiply')
def priceMultiply(number,numberOne):
    return number*numberOne

     