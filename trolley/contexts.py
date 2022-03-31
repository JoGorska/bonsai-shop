"""
context processor
"""
from decimal import Decimal
from django.conf import settings


def trolley_contents(request):
    """
    context processor:
    makes the content of the trolley available to all othe apps
    """
    trolley_items = []
    total = 0
    tree_count = 0

    context = {}

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': trolley_items,
        'total': total,
        'tree_count': tree_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
