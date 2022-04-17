"""
views for newsletter
"""
# pylint: disable=no-member
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponseRedirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Subscriber


@login_required
def subscribers(request):
    """
    view to return list of people that have signed up for newsletter page
    """
    subscriber_list = Subscriber.objects.order_by('-created_on')

    context = {
        'subscriber_list': subscriber_list,
    }
    return render(request, 'newsletter/subscribers.html', context)


def add_subscriber(request):
    """
    view to post the subscriber form to add the email to database
    """

    if request.method == 'POST':
        next_page = request.POST.get('next', '/')

        email = request.POST.get("email")
        subscribers = Subscriber.objects.all()

        for registered_subscriber in subscribers:
            if email == registered_subscriber.email:
                messages.error(
                    request,
                    'This email is already in our newsletter subscribers list')
            return HttpResponseRedirect(next_page)

        if "subscribed" in request.POST:
            subscribed = True
        else:
            subscribed = False

        if "accepted_privacy_policy" in request.POST:
            accepted_privacy_policy = True
        else:
            accepted_privacy_policy = False

        if "registered_user" in request.POST:
            user_id = request.POST.get("registered_user")
            registered_user = get_object_or_404(User, id=user_id)
        else:
            registered_user = None

        # creates instance of subscriber class
        subscriber = Subscriber(
            email=email,
            subscribed=subscribed,
            accepted_privacy_policy=accepted_privacy_policy,
            registered_user=registered_user
        )

        if subscriber.subscribed is False:
            messages.error(
                request,
                'Please mark the option that you wish to subscribe\
                 to newsletter')
            return HttpResponseRedirect(next_page)
        elif subscriber.accepted_privacy_policy is False:
            messages.error(
                request,
                'Please mark the option that you accept Privacy Policy')
            return HttpResponseRedirect(next_page)    
        else:
            subscriber.save()
            messages.success(
                request,
                f'Subscribed email {subscriber.email} to the newsletter')
            return HttpResponseRedirect(next_page)


@login_required
def unsubscribe(request, user_id):
    """
    view to change status of the email to unsubscribed
    for registered users
    """
    return HttpResponseRedirect('home')
