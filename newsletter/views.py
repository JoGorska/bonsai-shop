"""
views for newsletter
"""
# pylint: disable=no-member
from django.shortcuts import render
from .models import Subscriber


def subscribers(request):
    """
    view to return list of people that have signed up for newsletter page
    """
    subscriber_list = Subscriber.objects.order_by('-created_on')

    context = {
        'subscriber_list': subscriber_list,
    }
    return render(request, 'newsletter/subscribers.html', context)
