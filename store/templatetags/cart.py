from atexit import register
from django import template

register = template.Library()

@register.filter()
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==int(product.id):
            return True
    return False