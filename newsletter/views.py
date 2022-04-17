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
        print(f'what do we have here @{request.POST}')

        email = request.POST.get("email")
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
        next_page = request.POST.get('next', '/')
        # creates instance of subscriber class
        subscriber = Subscriber(
            email=email,
            subscribed=subscribed,
            accepted_privacy_policy=accepted_privacy_policy,
            registered_user=registered_user
        )

        if subscriber.subscribed == False:
            subscriber.save()


        return HttpResponseRedirect(next_page)
# add messages
# do not save instance when subscribed false or not accepted policy