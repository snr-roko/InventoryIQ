from django.db import models
from django.conf import settings
from storages.models import Warehouse, Store, Supplier

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='categories_created')

class WarehouseStock(models.Model):
    name = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='warehouse_stocks')
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    reorder_level = models.PositiveIntegerField()
    warehouse = models.ManyToManyField(Warehouse, related_name='warehouse_stocks', blank=True)
    supplier = models.ManyToManyField(Supplier, related_name='warehouse_stocks')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='warehouse_stocks_created')

    def __str__(self):
        return "{} at {} from {}".format(self.product_code, self.warehouse, self.supplier)

class StoreStock(models.Model):
    name = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='store_stocks')
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    reorder_level = models.PositiveIntegerField()
    store = models.ManyToManyField(Store, related_name='store_stocks', blank=True)
    supplier = models.ManyToManyField(Supplier, related_name='store_stocks')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='store_stocks_created')


    def __str__(self):
        return "{} at {} from {}".format(self.product_code, self.store, self.supplier)

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    product_image = models.ImageField(upload_to='product_images/', max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    reorder_level = models.PositiveIntegerField()

    def __str__(self):
        return self.product_code
        

