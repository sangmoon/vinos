from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=100)
    name_ko = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=2)
    reduced_price = models.IntegerField(null=True)
    official_price = models.IntegerField(null=True)
    extra_info = models.CharField(max_length=100, null=True)
    shop = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
