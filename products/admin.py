from django.contrib import admin
from .models import Product, ProductCategory, WarehouseStock, StoreStock

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(WarehouseStock)
admin.site.register(StoreStock)