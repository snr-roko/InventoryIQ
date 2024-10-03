from rest_framework import serializers
from .models import Warehouse, Store, Supplier

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        read_only_fields = ('created_by',)

class StoreSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Store
        fields = "__all__"
        read_only_fields = ('created_by',)

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Supplier
        fields = "__all__"
        read_only_fields = ('created_by',)