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
    path('edit/<int:question_id>/', views.edit_question, name='edit_question'),
    path('delete/<int:question_id>/',
          views.delete_question, name='delete_question'),
]
