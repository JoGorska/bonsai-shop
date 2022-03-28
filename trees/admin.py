"""
admin for trees app
"""
from django.contrib import admin
from.models import Feature, Enviroment, Tree


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    """
    class to enable admin manage the Tree model
    """
    list_display = ('id', 'name', 'price', 'current_stock', 'slug')
    search_fields = ['name', 'description']

    ordering = ('id',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    """
    class to enale admin manage Feature model
    """
    list_display = ('name', 'icon_fontawsome')


@admin.register(Enviroment)
class EnviromentAdmin(admin.ModelAdmin):
    """
    class to enable admin manage Enviroment model
    """
    list_display = ('name', 'icon_fontawsome')
