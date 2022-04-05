from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    '''
    admin for line item model
    admin can add and edit line items from inside the order model
    when we look at the order, we will see the list of editable line items
    without going to line item interface
    '''
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    '''
    admin for order model
    '''
    # this allows to vied and edit inline items inside each order
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_trolley', 'stripe_pid',)
    # this settings dictates the order in which the columns are displayed
    # in admin
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_trolley', 'stripe_pid',)
    # restrict the columns that show up in order list
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    # most recent orders at the top
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
