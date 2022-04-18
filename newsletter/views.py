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
        email_from_form = request.POST.get("email")
        email_to_lowercase = email_from_form.lower()
        email = email_to_lowercase.strip()
        print(f'EMAIL SHOULD BE LOWER CASE WITH NO SPACE{email}')
        all_subscribers = Subscriber.objects.all()
        all_emails_subscribed = []
        all_users_subscribed = []
        for subscriber in all_subscribers:
            all_emails_subscribed.append(subscriber.email)
            all_users_subscribed.append(subscriber.registered_user)
        print(f'TWO LISTS {all_emails_subscribed}, another one {all_users_subscribed}')
        # checks if email is already in database
        if email in all_emails_subscribed:
            current_subscriber = Subscriber.objects.filter(email=email)
            # email already in database and subscribed
            if current_subscriber.subscribed:
                messages.error(
                        request,
                        f'The email {email} is already in our database')
                return HttpResponseRedirect(next_page)
            # email in database, but currently unsubscribed
            else:
                current_subscriber.subscribed = True
                current_subscriber.save(update_fields=['subscribed'])
                messages.success(
                    request,
                    f'Successfully subscribed email {current_subscriber.email}\
                        to our newsletter')
                return HttpResponseRedirect(next_page)

        # email is not in database
        else:
            # check if user details have been passed in POST request
            if "registered_user" in request.POST:
                current_user = request.POST.get("registered_user")
                if current_user in all_users_subscribed:
                    # check if this user has registered another email already
                
                    current_subscriber = Subscriber.objects.filter(
                                                registered_user=current_user)
                    if current_subscriber.subscribed:
                        messages.error(
                                request,
                                f'The email {email} is already in our database')
                        return HttpResponseRedirect(next_page)
                    # email in database, but currently unsubscribed
                    else:
                        current_subscriber.subscribed = True
                        current_subscriber.save(update_fields=['subscribed'])
                        messages.success(
                            request,
                            f'Successfully subscribed email {current_subscriber.email}\
                                to our newsletter')
                        return HttpResponseRedirect(next_page)
                else:
                    # no user details in database, no email in database
                    registered_user = current_user
                    if "subscribed" in request.POST:
                        subscribed = True
                    else:
                        subscribed = False

                    if "accepted_privacy_policy" in request.POST:
                        accepted_privacy_policy = True
                    else:
                        accepted_privacy_policy = False
                    # creates instance of subscriber model class
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
                            'Please mark the option that you accept\
                                 Privacy Policy')
                        return HttpResponseRedirect(next_page)
                    else:
                        subscriber.save()
                        messages.success(
                            request,
                            f'Subscribed email {subscriber.email}\
                            to the newsletter')

                        return HttpResponseRedirect(next_page)

            else:
                # no user details in request, no email in database
                registered_user = None
                if "subscribed" in request.POST:
                    subscribed = True
                else:
                    subscribed = False

                if "accepted_privacy_policy" in request.POST:
                    accepted_privacy_policy = True
                else:
                    accepted_privacy_policy = False
                # creates instance of subscriber model class
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
                        f'Subscribed email {subscriber.email}\
                          to the newsletter')

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
                    from our newsletter')

        except Subscriber.DoesNotExist:
            messages.error(
                request,
                f'The email {email} is not on our list of subscribers')
            return HttpResponseRedirect(next_page)

        return HttpResponseRedirect(next_page)
