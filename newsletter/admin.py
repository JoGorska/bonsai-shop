"""
admin for newsletter app
"""

from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    '''
    class enabling admin see the Subscriber model in admin panel
    '''
    list_display = ('email', 'registered_user', 'created_on',)
    search_fields = ['email']
    list_filter = ('accepted_privacy_policy', 'subscribed')
