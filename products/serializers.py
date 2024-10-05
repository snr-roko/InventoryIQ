from rest_framework import serializers
from .models import WarehouseStock, StoreStock, Product, ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        read_only_fields = ("created_by",)

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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("quantity",)