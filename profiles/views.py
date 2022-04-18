# pylint: disable=no-member
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from newsletter.models import Subscriber


@login_required
def profile(request):
    """
    Display the user's profile
    """
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=user_profile)

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()
    # get the list of all subscribers filters if current user is on the list
    subscribers = Subscriber.objects.filter(registered_user=current_user)
    subscribed = False
    if subscribers.count() > 0:
        subscribed = True

    print(f'CHECK ME IF I HAVE SUBSCRIBED {subscribed}')
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_profile': user_profile,
        'subscribed': subscribed,
    }
    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    display order history in the checkout success template
    """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past comnfirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
