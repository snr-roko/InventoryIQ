from django.contrib import admin
from .models import Warehouse, Store, Supplier

admin.site.register(Warehouse)
admin.site.register(Store)
admin.site.register(Supplier)