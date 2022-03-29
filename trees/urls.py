"""
urls for trees app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_trees, name='all_trees'),
    path('<tree_id>', views.tree_detail, name='tree_detail'),
]
