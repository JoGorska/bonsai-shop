"""
views for trees appp
"""
from django.shortcuts import render
from .models import Tree


def all_trees(request):
    """
    view to show all trees,
    including sorting and search queries
    """
    trees = Tree.objects.all()

    context = {
        'trees': trees,
    }
    return render(request, 'trees/trees.html', context)
