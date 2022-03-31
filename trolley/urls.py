"""
urls for trolley app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_trolley, name='view_trolley'),
]
