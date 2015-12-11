from django.db import models

class Uncles(models.Model):
    first_name = models.CharField("First", max_length=255, blank=True, null=True, )
    last_name = models.CharField("Last", max_length=255, blank=True, null=True, )
    def classname(self):
        classname = self.__class__.__name__
        return classname

    class Meta:
        verbose_name = 'Uncle'
        verbose_name_plural = 'Uncles'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)