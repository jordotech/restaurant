from django.contrib import admin
from .models import *

class RestaurantAdmin(admin.ModelAdmin):
    def average(self, object):
        ws=object.waittime_set.all()
        count = object.waittime_set.count()
        if count < 1:
            return 0
        total = 0
        for w in ws:
            total += w.waittime
        return total/count
    list_display = ('id', 'name', 'province', 'average')
    #ordering = ['postalcode', ]
    list_filter = ['province',]
    search_fields = ('name',)

class WaittimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'waittime', 'created')

admin.site.register(Restaurants, RestaurantAdmin)
admin.site.register(Waittime, WaittimeAdmin)
