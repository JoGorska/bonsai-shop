"""
views for checkout app
"""
import json
import stripe

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from trees.models import Tree
from .forms import OrderForm
from .models import Order, OrderLineItem
from trolley.contexts import trolley_contents


def checkout(request):
    """
    view to make checkout
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        trolley = request.session.get('trolley', {})
        # collects data directly from theform as per each post item
        # this is done manually to skip save info checkbox
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # saves the form data into the instance of order form
        order_form = OrderForm(form_data)
        # checks if form with the form data passes the validation 
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_trolley = json.dumps(trolley)
            order.save()
        # need to iterate through each trolley item to create line item
            for item_id, item_data in trolley.items():
                try:
                    tree = Tree.objects.get(id=item_id)

                    order_line_item = OrderLineItem(
                        order=order,
                        tree=tree,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Tree.DoesNotExist:
                    messages.error(request, (
                        "One of the trees in your trolley wasn't found \
                         in our database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_trolley'))
            # gets the option if the user has clicked to save info
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        # if order form isn't valid
        else:
            messages.error(request, 'There was an error with your form. \
                                     Please double check your information.')
 
    else:
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
