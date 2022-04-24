"""
urls for trolley app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_trolley, name='view_trolley'),
    path('add/<int:tree_id>/', views.add_to_trolley, name='add_to_trolley'),
    path('update/<int:tree_id>/', views.update_trolley, name='update_trolley'),
    path('remove/<int:tree_id>/',
         views.remove_from_trolley, name='remove_from_trolley'),
]
