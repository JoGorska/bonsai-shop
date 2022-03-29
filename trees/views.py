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
    all_features = Feature.objects.all()
    all_enviroments = Enviroment.objects.all()

    query = None
    current_features = None
    current_enviroments = None
    current_types = None

    if request.GET:
        # filters results by given feature
        # add error handling if feature not found???
        if 'feature' in request.GET:
            features = request.GET['feature'].split(',')
            trees = trees.filter(feature__name__in=features)
            current_features = Feature.objects.filter(name__in=features)

        elif 'enviroment' in request.GET:
            enviroments = request.GET['enviroment'].split(',')
            trees = trees.filter(enviroment__name__in=enviroments)
            current_enviroments = Enviroment.objects.filter(
                                            name__in=enviroments)
        elif 'type' in request.GET:
            type = request.GET['type']
            trees = Tree.objects.filter(leaves_or_needles=type)

        # query to search both product name and description and return results
        # if the q was found in either product name or description
        elif 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter \
                                         any search criteria!")
                return redirect(reverse('all_trees'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
                )
            trees = trees.filter(queries)

    context = {
        'trees': trees,
        'features': all_features,
        'enviroments': all_enviroments,
        'search_term': query,
        'current_features': current_features,
        'current_enviroments': current_enviroments,
        'current_types': current_types,
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
