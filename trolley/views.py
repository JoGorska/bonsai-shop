"""
views for trolley app
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from trees.models import Tree


def view_trolley(request):
    """
    view to return trolley content page
    """
    return render(request, 'trolley/trolley.html')


def add_to_trolley(request, tree_id):
    """
    Add a specified quantity of the tree to the trolley
    """
    tree = Tree.objects.get(pk=tree_id)
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
        messages.success(request, f'Added {tree.name} to your bag')

    request.session['trolley'] = trolley

    return redirect(redirect_url)


def update_trolley(request, tree_id):
    """
    Update quantity of items in the trolley
    """
    quantity = int(request.POST.get('quantity'))
    # checks if trolley already exists in session
    # if it doesn't it creates one
    # sets the quantity to the new value
    trolley = request.session.get('trolley', {})
    # html validation should prevent submitting form below 1, this is
    # just in case if form is submitted programatically
    if quantity > 0:
        trolley[tree_id] = quantity
    else:
        trolley.pop(str(tree_id))

    request.session['trolley'] = trolley

    return redirect(reverse('view_trolley'))


def remove_from_trolley(request, tree_id):
    """
    Removes item from trolley
    """
    trolley = request.session.get('trolley', {})
    trolley.pop(str(tree_id))
    request.session['trolley'] = trolley

    return redirect(reverse('view_trolley'))
