"""
urls for questions app
"""
# pylint: disable=no-member
from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuestionsList.as_view(), name='questions'),
    path('add/', views.AddNewQuestion.as_view(), name='add_question'),
]
