"""
context processor
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from trees.models import Tree


def trolley_contents(request):
    """
    context processor:
    makes the content of the trolley available to all othe apps
    """
    trolley_items = []
    total = 0
    tree_count = 0
    trolley = request.session.get('trolley', {})

    for tree_id, quantity in trolley.items():
        tree = get_object_or_404(Tree, pk=tree_id)
        total += quantity * tree.price
        tree_count += quantity
        trolley_items.append({
            'tree_id': tree_id,
            'quantity': quantity,
            'tree': tree,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'trolley_items': trolley_items,
        'total': total,
        'tree_count': tree_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
