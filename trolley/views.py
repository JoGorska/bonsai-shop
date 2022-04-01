"""
views for trolley app
"""
from django.shortcuts import render, redirect


def view_trolley(request):
    """
    view to return trolley content page
    """
    return render(request, 'trolley/trolley.html')


def add_to_trolley(request, tree_id):
    """
    Add a specified quantity of the tree to the trolley
    """
    quantity = int(request.POST.get('quantity'))
    # this variable redirect_url is to redirect the user back to the same page
    # after the product is added to trolley
    redirect_url = request.POST.get('redirect_url')
    # checks if trolley already exists in session
    # if it doesn't it creates one
    trolley = request.session.get('trolley', {})

    if tree_id in list(trolley.keys()):
        trolley[tree_id] += quantity
    else:
        trolley[tree_id] = quantity

    request.session['trolley'] = trolley

    return redirect(redirect_url)
