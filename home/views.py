"""
views for home app
"""
from django.shortcuts import render


def index_view(request):
    """
    view to return index page
    """
    return render(request, 'home/index.html')
