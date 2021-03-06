"""
urls for questions app
"""
# pylint: disable=no-member
from django.urls import path
from . import views


urlpatterns = [
    path('subscribers', views.subscribers, name='subscribers'),
    path('add_subscriber', views.add_subscriber, name='add_subscriber'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('unsubscribe_registered_user', views.unsubscribe_registered_user,
         name='unsubscribe_registered_user'),
    path('send_newsletter', views.send_newsletter, name='send_newsletter'),

]
