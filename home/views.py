"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import render
from questions.models import Question


def index_view(request):
    """
    view to return index page
    """
    questions = Question.objects.filter(status=1).order_by('-created_on')
    context = {
        'questions': questions,
    }
    return render(request, 'home/index.html', context)
