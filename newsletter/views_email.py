# email view based on django documentation found here:
# https://docs.djangoproject.com/en/3.2/topics/email/#preventing-header-injection
@login_required
def send_newsletter(request):
    """
    view for superuser to send newsletters
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owners can do that.')
        return redirect(reverse('questions'))

    faq_latest_question = Question.objects.filter(status=1).first()

    newsletter_subscribers = Subscriber.objects.filter(subscribed=True)

    for subscriber in newsletter_subscribers:
        subject = render_to_string(
                'newsletter/newsletter_emails/newsletter_email_subject.txt',
                {'faq_latest_question': faq_latest_question,
                 'subscriber': subscriber})

        body = render_to_string(
            'newsletter/newsletter_emails/newsletter_email_body.txt',
            {'faq_latest_question': faq_latest_question,
             'subscriber': subscriber,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        if subject and body and subscriber.email:
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email]
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/questions/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')