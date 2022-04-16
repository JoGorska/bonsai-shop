"""
urls for questions app
"""
# pylint: disable=no-member
from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuestionsList.as_view(), name='questions'),
    path('manager/', views.questions_manager, name='questions_manager'),
    path('add/', views.add_question, name='add_question'),
]
