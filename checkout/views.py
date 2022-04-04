"""
views for checkout app
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe

from .forms import OrderForm
from trolley.contexts import trolley_contents


def checkout(request):
    """
    view to make checkout
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    trolley = request.session.get('trolley', {})
    if not trolley:
        messages.error(request,
                       "There's nothing in your trolley at the moment")
        return redirect(reverse('all_trees'))

    current_trolley = trolley_contents(request)
    total = current_trolley['grand_total']
    stripe_total = round(total * 100)
    # sets the secret key on stripe
    stripe.api_key = stripe_secret_key
    # creates payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(f'PAYMENT INTENT {intent}')

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
