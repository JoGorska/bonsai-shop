"""
views for newsletter
"""
# pylint: disable=no-member
# pylint: disable=invalid-name
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
        all_subscribers = Subscriber.objects.all()
        # checks if email in newsletter database
        for registered_subscriber in all_subscribers:
            if email == registered_subscriber.email:
                # checks if email has status subscribed
                if registered_subscriber.subscribed:
                    messages.error(
                        request,
                        'This email is already in our newsletter subscribers list')
                    return HttpResponseRedirect(next_page)
                # if email is in database, but has unsubscribed status
                # gets this object and updates it to be subscribed
                else:
                    already_in_database_subscriber = Subscriber.objects.get(email=email)
                    already_in_database_subscriber.subscribed = False
                    already_in_database_subscriber.save(update_fields=['subscribed'])
                    messages.success(
                        request,
                        f'Subscribed email {already_in_database_subscriber.email} to the newsletter')
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

        messages.success(
            request,
            f'Subscribed email {subscriber.email} to the newsletter')
        subscriber.save()

        return HttpResponseRedirect(next_page)


def unsubscribe(request):
    """
    view to change status of the email to unsubscribed
    """
    if request.method == 'POST':
        next_page = request.POST.get('next', '/')
        email = request.POST.get("email")
        try:
            current_subscriber = Subscriber.objects.get(email=email)
            print(f'CURRENT SUBSCRIBER{current_subscriber.subscribed}')
            current_subscriber.subscribed = False
            current_subscriber.save(update_fields=['subscribed'])
            print(f'CURRENT SUBSCRIBER AFTER{current_subscriber.subscribed}')
            messages.success(
                request,
                f'Successfully unsubscribed email {current_subscriber.email}\
                    froum our newsletter')

        except Subscriber.DoesNotExist:
            messages.error(
                request,
                f'The email {email} is not on our list of subscribers')
            return HttpResponseRedirect(next_page)

        return HttpResponseRedirect(next_page)
