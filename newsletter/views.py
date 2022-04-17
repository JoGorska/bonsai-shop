"""
views for newsletter
"""
# pylint: disable=no-member
from django.shortcuts import render


def signees(request):
    """
    view to return list of people that have signed up for newsletter page
    """
    return render(request, 'newsletter/signees.html')
