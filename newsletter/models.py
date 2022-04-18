"""
Models for newsletter
"""

from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
    """
    creates a table of subscribers that have signed up to newsletter
    """

    email = models.EmailField(max_length=254, blank=False, null=False)
    # user can set unsubscribed or can choose for this data to be deleted
    subscribed = models.BooleanField(default=False, blank=False, null=False)
    # I keep the record that they have actively accepted privacy policy
    accepted_privacy_policy = models.BooleanField(default=False,
                                                  blank=False, null=False)
    # allows foreign key to be Null if subscriber isn't a registered user
    registered_user = models.ForeignKey(
                User, on_delete=models.SET_NULL, blank=True, null=True,
                related_name='newsletter_subscriber')
    created_on = models.DateTimeField(auto_now=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
