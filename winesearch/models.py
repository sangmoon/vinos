from django.db import models
from .bordeax import BordeauxCru, BordeauxRegion


class Producer(models.Model):
    """
    Class for wine producer. it can be chateau, domaine, etc
    """
    name = models.CharField(name="name", max_length=100)
    cru = models.CharField(name="cru", max_length=100,
                           choices=[(cru, cru.value) for cru in BordeauxCru])
    region = models.CharField(name="region", max_length=100,
                              choices=[(region, region.value) for region in BordeauxRegion])

    def __str__(self):
        return "name: %s cru: %s region: %s" % (self.name, self.cru, self.region)


class Wine(models.Model):
    """
    Class for Wine
    """
    name = models.CharField(name='name', max_length=100)
    country = models.CharField(name='country', max_length=20)
    region = models.CharField(name='region', max_length=100)
    producer = models.ForeignKey(Producer, blank=True, null=True, on_delete=models.SET_NULL())

    def __str__(self):
        return "name:%s country:%s region:%s producer:%s" % (self.name, self.country, self.region, self.producer)




