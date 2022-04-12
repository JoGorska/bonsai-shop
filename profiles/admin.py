from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    '''
    admin for User Profile
    '''

    fields = ('user', 'default_street_address1')
    # restrict the columns that show up in order list
    list_display = ('user', 'default_street_address1', )

    # ordering = ('-date',)


admin.site.register(UserProfile)
