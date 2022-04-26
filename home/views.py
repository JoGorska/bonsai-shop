"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import render
from questions.models import Question
from newsletter.models import Subscriber


def index_view(request):
    """
    view to return index page
    """
    questions = Question.objects.filter(status=1).order_by('-created_on')
    subscribed = False
    if request.user.is_authenticated:
        user = request.user
        if Subscriber.objects.filter(
                registered_user=user).filter(subscribed=True).exists():
            subscribed = True

    context = {
        'questions': questions,
        'subscribed': subscribed,
    }
    return render(request, 'home/index.html', context)

def render_404(request):
    return render(request, 'home/404.html')
