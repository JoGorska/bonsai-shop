"""
views for trees appp
"""
from django.shortcuts import render, get_object_or_404
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


def tree_detail(request, tree_id):
    """
    view to show details of one tree
    """
    tree = get_object_or_404(Tree, id=tree_id)

    context = {
        'tree': tree,

    }
    return render(request, 'trees/tree_detail.html', context)
