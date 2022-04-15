"""
admin for questions app
"""

from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''
    class enabling admin see the Question model with details and search fields
    '''
    list_display = ('author', 'header', 'created_on', 'status')
    search_fields = ['header', 'content']
    list_filter = ('status', 'created_on')
