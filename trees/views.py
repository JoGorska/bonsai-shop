"""
views for trees appp
"""
from django.shortcuts import render
from .models import Tree, Feature, Enviroment


def all_trees(request):
    """
    view to show all trees,
    including sorting and search queries
    """
    trees = Tree.objects.all()
    features = Feature.objects.all()
    enviroments = Enviroment.objects.all()

    context = {
        'trees': trees,
        'features': features,
        'enviroments': enviroments,
    }
    return render(request, 'trees/trees.html', context)
