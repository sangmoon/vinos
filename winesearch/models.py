from django.db import models

# Create your models here.


class Wine(models.Model):
    name = models.CharField(name='Name', max_length=100)
    country = models.CharField(name='Country', max_length=20)
    price = models.DecimalField(name='price')


class GrapeType:
    pass
