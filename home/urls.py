"""
urls for home app
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='home'),
    path('test', views.render_404, name='render_404')
]
