"""
views for trees appp
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Tree, Feature, Enviroment


def all_trees(request):
    """
    view to show all trees,
    including sorting and search queries
    """
    trees = Tree.objects.all()
    features = Feature.objects.all()
    enviroments = Enviroment.objects.all()

# query to search both product name and description and return results
# if the q was found in either product name or description
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter \
                                         any search criteria!")
                return redirect(reverse('all_trees'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
                )

    context = {
        'trees': trees,
        'features': features,
        'enviroments': enviroments,
        'search_term': query,
    }
    return render(request, 'trees/trees.html', context)


def tree_detail(request, tree_id):
    """
    view to show details of one tree
    """
    tree = get_object_or_404(Tree, id=tree_id)

    context = {
        'tree': tree,

    }
    return render(request, 'trees/tree_detail.html', context)
