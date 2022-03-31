"""
views for trolley app
"""
from django.shortcuts import render


def view_trolley(request):
    """
    view to return trolley content page
    """
    return render(request, 'trolley/trolley.html')
