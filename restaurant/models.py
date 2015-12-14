from django.db import models

class Restaurants(models.Model):
    name = models.CharField("Name", max_length=255, blank=True, null=True)
    street = models.CharField(('Street'), max_length=140, blank=True, null=True)
    city = models.CharField(('City'), max_length=180, blank=True, null=True)
    province = models.CharField(('Province'), max_length=180, blank=True, null=True)
    postalcode = models.CharField(('Postal Code'), max_length=20, blank=True)
    iso = models.CharField(('Country'), max_length=2, blank=True, null=True)
    latitude = models.FloatField(('latitude'), blank=True, null=True)
    longitude = models.FloatField(('longitude'), blank=True, null=True)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __unicode__(self):
        return self.name


class Waittime(models.Model):
    restaurant = models.ForeignKey(Restaurants, related_name='waittime_set')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    waittime = models.IntegerField(blank=True,null=True, help_text=("Wait time in seconds."))

    def __unicode__(self):
        return '%s waittime' % (self.restaurant)