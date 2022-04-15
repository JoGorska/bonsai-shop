"""
views for home app
"""
from django.shortcuts import render


def questions(request):
    """
    view to display all questions to the user
    """
    return render(request, 'questions/questions.html')

