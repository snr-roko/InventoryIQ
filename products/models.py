from django.db import models
from django.conf import settings
from storages.models import Warehouse, Store, Supplier
from django.utils import timezone

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='categories_created')

    def __str__(self):
        return self.name

class WarehouseStock(models.Model):
    name = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='warehouse_stocks')
    active = models.BooleanField(default=True)
    low_stock = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    reorder_level = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name='warehouse_stocks', null=True, blank=True)
    supplier = models.ManyToManyField(Supplier, related_name='warehouse_stocks', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='warehouse_stocks_created')

    class Meta:
        unique_together = ("stock_code", "warehouse")
    
    def __str__(self):
        return "{} at {}".format(self.product_code, self.warehouse)

class StoreStock(models.Model):
    name = models.CharField(max_length=255)
    stock_code = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='store_stocks') 
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    low_stock = models.BooleanField(default=False)    
    reorder_level = models.PositiveIntegerField()
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='store_stocks', null=True, blank=True)
    supplier = models.ManyToManyField(Supplier, related_name='store_stocks', blank=True)
    barcode = models.CharField(max_length=13, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='store_stocks_created')

    class Meta:
        unique_together = ("stock_code", "store")

    def __str__(self):
        return "{} at {}".format(self.product_code, self.store)

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    product_image = models.ImageField(upload_to='product_images/', max_length=255, null=True, blank=True)
    low_stock = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    reorder_level = models.PositiveIntegerField()
    low_stock = models.BooleanField(default=False)
    last_active_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product_code
        
    def deactivate(self):
        self.active = False
        self.last_active_date = timezone.now()
        self.save()
