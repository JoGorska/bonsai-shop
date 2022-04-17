"""
views for newsletter
"""
# pylint: disable=no-member
from django.shortcuts import render


def signees(request):
    """
    view to return list of people that have signed up for newsletter page
    """
    

    context = {
        'signee_list': signee_list,
    }
    return render(request, 'newsletter/signees.html')
