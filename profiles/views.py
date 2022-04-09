from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """
    Display the user's profile
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()
    print(f'ORDERS {orders}')
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_profile': user_profile
    }
    return render(request, template, context)


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
