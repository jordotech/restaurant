from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'province', 'average')
    #ordering = ['postalcode', ]
    list_filter = ['province',]
    search_fields = ('name',)

class WaittimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'waittime', 'created', 'user')

admin.site.register(Restaurants, RestaurantAdmin)
admin.site.register(Waittime, WaittimeAdmin)
