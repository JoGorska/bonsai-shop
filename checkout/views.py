"""
views for checkout app
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    """
    view to make checkout
    """
    trolley = request.session.get('trolley', {})
    if not trolley:
        messages.error(request,
                       "There's nothing in your trolley at the moment")
        return redirect(reverse('all_trees'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
