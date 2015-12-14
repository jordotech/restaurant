from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'province',)
    #ordering = ['postalcode', ]
    #list_filter = ['iso', ]
    #search_fields = ('state', 'city', 'iso', 'postalcode')

class WaittimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'waittime', 'created')

admin.site.register(Restaurants, RestaurantAdmin)
admin.site.register(Waittime, WaittimeAdmin)
