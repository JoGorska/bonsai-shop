from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


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
