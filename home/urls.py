"""
urls for home app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='home'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
]
