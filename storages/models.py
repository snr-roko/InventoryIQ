from django.db import models
from django.conf import settings

class Warehouse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # set to null temporarily for testing purposes
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='warehouses_created', null=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # set to null temporarily for testing purposes
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='stores_created', null=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    # set to null temporarily for testing purposes
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='suppliers_created', null=True)

    def __str__(self):
        return self.name