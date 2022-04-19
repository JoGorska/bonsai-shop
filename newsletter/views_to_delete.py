def delete_second(request):
    """
    view to post the subscriber form to add the email to database
    """

    if request.method == 'POST':
        next_page = request.POST.get('next', '/')
        # clean email data
        email_from_form = request.POST.get("email")
        email_to_lowercase = email_from_form.lower()
        email = email_to_lowercase.strip()
        # get all subscribers
        all_subscribers = Subscriber.objects.all()
        all_emails_subscribed = []
        all_users_subscribed = []
        for subscriber in all_subscribers:
            all_emails_subscribed.append(subscriber.email)
            all_users_subscribed.append(subscriber.registered_user)


        if email in all_emails_subscribed:
            # if need to get the subscriber object to check if it has opt in newsletter
            email_already_in_database

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

        messages.success(
            request,
            f'Subscribed email {subscriber.email} to the newsletter')
        subscriber.save()

        return HttpResponseRedirect(next_page)


def delete_me(request):
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
            current_subscriber = get_object_or_404(Subscriber, email=email)
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



def add_subscriber(request):
    """
    view to post the subscriber form to add the email to database
    """
    next_page = request.POST.get('next', '/')


    # gets email from request and generates lists for for further validation
    # clean email data
    email_from_form = request.POST.get("email")
    email_to_lowercase = email_from_form.lower()
    email = email_to_lowercase.strip()
    print(f'EMAIL SHOULD BE LOWER CASE WITH NO SPACE{email}')

    try:

        # validates if both options are checked
        if "subscribed" in request.POST:
            subscribed = True
        else:
            messages.error(
                    request,
                    'Please mark the option that you wish to subscribe\
                    to newsletter')
            return HttpResponseRedirect(next_page)

        if "accepted_privacy_policy" in request.POST:
            accepted_privacy_policy = True
        else:
            messages.error(
                    request,
                    'Please mark the option that you accept Privacy Policy')
            return HttpResponseRedirect(next_page)
        
        # email already in database but not subscribed
        current_subscriber = Subscriber.objects.filter(email=email).filter(subscribed=False)
        current_subscriber.subscribed = True
        current_subscriber.save(update_fields=['subscribed'])
        messages.success(
            request,
            f'Successfully subscribed email {current_subscriber.email}\
                to our newsletter')
        return HttpResponseRedirect(next_page)

    except Exception as e:
        current_subscriber = Subscriber.objects.filter(email=email).filter(subscribed=True)
        # email already in database and subscribed
        messages.error(
                request,
                f'The email {email} is already in our database')
        return HttpResponseRedirect(next_page)

    else:
        # check if user is in request
        if "registered_user" in request.POST:
            user_id = request.POST.get("registered_user")
            registered_user = get_object_or_404(User, id=user_id)

            try:
                # user is already in database but not subscribed
                current_subscriber = Subscriber.objects.filter(registered_user=registered_user).filter(subscribed=False)
                current_subscriber.subscribed = True
                current_subscriber.save(update_fields=['subscribed'])
                messages.success(
                    request,
                    f'Successfully subscribed email {current_subscriber.email}\
                        to our newsletter')
                return HttpResponseRedirect(next_page)

            except Exception as e:
                current_subscriber = Subscriber.objects.filter(
                    registered_user=registered_user).filter(subscribed=True)
                # user already in database and subscribed, but different email
                messages.error(
                        request,
                        f'You have already registered {current_subscriber.email} to receive newsletter')
                return HttpResponseRedirect(next_page)

            else:
                # create new subscriber with registered user
                # creates instance of subscriber class
                subscriber = Subscriber(
                    email=email,
                    subscribed=subscribed,
                    accepted_privacy_policy=accepted_privacy_policy,
                    registered_user=registered_user
                    )
                subscriber.save()
                messages.success(
                    request,
                    f'Subscribed email {subscriber.email} to the newsletter')
                return HttpResponseRedirect(next_page)
        
        # user is not in request
        else:
            subscriber = Subscriber(
                email=email,
                subscribed=subscribed,
                accepted_privacy_policy=accepted_privacy_policy,
                registered_user=registered_user
                )
            subscriber.save()
            messages.success(
                request,
                f'Subscribed email {subscriber.email} to the newsletter')
            return HttpResponseRedirect(next_page)
    
    finally:
        messages.error(
                request,
                f'Please make sure the form is valid')
        return HttpResponseRedirect(next_page)