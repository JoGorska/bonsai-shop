import json
from django.http import HttpResponse

from .models import Order, OrderLineItem
from trees.models import Tree


class StripeWHHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        trolley = intent.metadata.trolley
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        # replace any empty strings with value None
        # stripe will store them as blank strings
        # we want Null value in database
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        try:
            order_exists = False
            # try to get object from the database
            # iexact - case insensitive
            order = Order.objects.get(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        county__iexact=shipping_details.address.state,
                        grand_total=grand_total,
                        original_trolley=trolley,
                        stripe_pid=pid,
                    )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: verified order already in database',
                status=200)

        except Order.DoesNotExist:
            # creates a new order
            order = None
            try:
                order = Order.objects.create(
                            full_name=shipping_details.name,
                            email=billing_details.email,
                            phone_number=shipping_details.phone,
                            country=shipping_details.address.country,
                            postcode=shipping_details.address.postal_code,
                            town_or_city=shipping_details.address.city,
                            street_address1=shipping_details.address.line1,
                            street_address2=shipping_details.address.line2,
                            county=shipping_details.address.state,
                            original_trolley=trolley,
                            stripe_pid=pid,
                        )

                for item_id, item_data in json.loads(trolley).items():
                    tree = Tree.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        tree=tree,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    # deletes order if any errors occured and 
                    # returns 500 error response to stripe
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
