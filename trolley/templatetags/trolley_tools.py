"""
custom template tags enabling calculating subtotal in the bag
"""

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    '''
    calculates subtotal for the particular item,
    takes price and quantity as arguments
    '''
    return price * quantity
