"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib.auth.models import User
from newsletter.models import Subscriber
from questions.models import Question


def index_view(request):
    """
    view to return index page, returns questions in the context and checks
    if the user has registered
    """
    questions = Question.objects.filter(status=1).order_by('-created_on')
    all_subscribers = Subscriber.objects.all()
    subscribed = False
    if request.user:
        user_from_request = request.user
        current_user = get_object_or_404(User, username=user_from_request)

        for subscriber in all_subscribers:
            if str(subscriber.registered_user) == str(current_user.username):
                if subscriber.subscribed is True:
                    subscribed = True

    context = {
        'questions': questions,
        'subscribed': subscribed,
    }
    return render(request, 'home/index.html', context)
