"""
admin for trees app
"""
from django.contrib import admin
from.models import Feature, Enviroment, Tree


admin.site.register(Tree)
admin.site.register(Feature)
admin.site.register(Enviroment)
