"""
urls for trees app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_trees, name='all_trees'),
    path('detail/<str:tree_slug>/', views.tree_detail, name='tree_detail'),
    path('add/', views.add_tree, name='add_tree'),
    path('edit/<str:tree_slug>/', views.edit_tree, name='edit_tree'),
    path('delete/<str:tree_slug>/', views.delete_tree, name='delete_tree'),
]
