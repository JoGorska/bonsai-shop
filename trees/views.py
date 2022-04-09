"""
views for trees appp
"""
# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Tree, Feature, Enviroment
from .forms import TreeForm


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
    sort = None
    direction = None

    if request.GET:
        # filters results by given feature
        # add error handling if feature not found???

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                trees = trees.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            trees = trees.order_by(sortkey)

        elif 'feature' in request.GET:
            features = request.GET['feature'].split(',')
            trees = trees.filter(feature__name__in=features)
            current_features = Feature.objects.filter(name__in=features)

        elif 'enviroment' in request.GET:
            enviroments = request.GET['enviroment'].split(',')
            trees = trees.filter(enviroment__name__in=enviroments)
            current_enviroments = Enviroment.objects.filter(
                                            name__in=enviroments)
        elif 'type' in request.GET:
            leaves_or_needles = request.GET['type']
            trees = Tree.objects.filter(leaves_or_needles=leaves_or_needles)

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

    current_sorting = f'{sort}_{direction}'
    # gets trolley from the session or creates empty dictionary
    # than makes a list of keys containing the ids of the trees in the trolley
    trolley = request.session.get('trolley', {})
    trees_in_bag_strings = list(trolley.keys())
    trees_in_bag = list(map(int, trees_in_bag_strings))

    context = {
        'trees': trees,
        'features': all_features,
        'enviroments': all_enviroments,
        'search_term': query,
        'current_features': current_features,
        'current_enviroments': current_enviroments,
        'current_types': current_types,
        'current_sorting': current_sorting,
        'trees_in_bag': trees_in_bag,
    }
    return render(request, 'trees/trees.html', context)


def tree_detail(request, tree_slug):
    """
    view to show details of one tree
    """
    tree = get_object_or_404(Tree, slug=tree_slug)
    # need for loop to get the features as it is many to many field
    # off a particular tree as tree may have more than one feature
    features = []

    if tree.feature:
        for feature in tree.feature.all():
            features.append(feature)

    # gets trolley from the session or creates empty dictionary
    # than makes a list of keys containing the ids of the trees in the trolley
    trolley = request.session.get('trolley', {})
    trees_in_bag_strings = list(trolley.keys())
    trees_in_bag = list(map(int, trees_in_bag_strings))
    # I need quantity in bag if the tree is already in bag
    # to display the quantity from the bag
    quantity_in_bag = 0
    for item in trolley:
        if int(item) == tree.id:
            quantity_in_bag = trolley[item]

    context = {
        'tree': tree,
        'features': features,
        'trees_in_bag': trees_in_bag,
        'quantity_in_bag': quantity_in_bag,

    }
    return render(request, 'trees/tree_detail.html', context)


def add_tree(request):
    """
    Add tree to the store
    """
    if request.method == 'POST':
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            tree = form.save()
            messages.success(request, 'Successfully added tree!')
            return redirect(reverse('tree_detail', args=[tree.slug]))
        else:
            messages.error(request, 'Failed to add tree.\
                                     Please ensure the form is valid')
    else:
        form = TreeForm()

    template = 'trees/add_tree.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_tree(request, tree_slug):
    """
    edits the tree that is already in database
    """
    tree = get_object_or_404(Tree, slug=tree_slug)

    if request.method == 'POST':
        form = TreeForm(request.POST, request.FILES, instance=tree)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the tree details!')
            return redirect(reverse('tree_detail', args=[tree.slug]))
        else:
            messages.error(request, 'Failed to update the tree details.\
                                     Please ensure the form is valid.')
    else:
        form = TreeForm(instance=tree)
        messages.info(request, f'You are editing {tree.name}')

    template = 'trees/edit_tree.html'
    context = {
        'form': form,
        'tree': tree,
    }
    return render(request, template, context)


def delete_tree(request, tree_slug):
    """
    deletes the tree from database
    """
    tree = get_object_or_404(Tree, slug=tree_slug)
    tree.delete()
    messages.success(request, f'Successfully deleted the tree {tree.name}')
    return redirect(reverse('all_trees'))
