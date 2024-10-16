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
        read_only_fields = ("quantity", "created_by", "low_stocks")
    
    # We validate barcodes to make sure only 13 characters are entered.
    def validate_barcode(self, value):
        if len(value) != 13:
            return serializers.ValidationError("Barcode must be 13 characters")
        return value

class StoreStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreStock
        fields = "__all__"
        read_only_fields = ("quantity", "created_by", "low_stocks")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("quantity", "low_stocks")