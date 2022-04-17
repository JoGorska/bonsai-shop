"""
urls for questions app
"""
# pylint: disable=no-member
from django.urls import path
from . import views


urlpatterns = [
    path('subscribers', views.subscribers, name='subscribers'),
    path('add_subscriber', views.add_subscriber, name='add_subscriber'),
]
