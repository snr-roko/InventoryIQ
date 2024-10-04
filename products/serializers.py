from rest_framework import serializers
from .models import WarehouseStock, StoreStock, Product


class WarehouseStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseStock
        fields = "__all__"
        read_only_fields = ("quantity", "created_by")

class StoreStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreStock
        fields = "__all__"
        read_only_fields = ("quantity", "created_by")

class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("quantity", "created_by")
