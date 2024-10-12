from rest_framework import serializers
from products.models import WarehouseStock, StoreStock

class WarehouseStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseStock
        fields = ('name', 'stock_code', 'category', 'quantity', 'active', 'reorder_level', 'warehouse', 'supplier')

class StoreStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreStock
        fields = ('name', 'stock_code', 'category', 'quantity', 'active', 'reorder_level', 'store', 'supplier')

