"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import render
from django.views import generic, View
from .models import Question


class QuestionsList(generic.ListView):
    """
    view to display all questions paginated
    """
    model = Question
    queryset = Question.objects.filter(status=1).order_by('-created_on')
    template_name = 'questions/questions.html'
    paginate_by = 10
