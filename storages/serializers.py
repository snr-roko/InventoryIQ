from rest_framework import serializers
from .models import Warehouse, Store, Supplier

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        read_only_fields = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Warehouse.objects.create(**validated_data)

class StoreSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Store
        fields = "__all__"
        read_only_fields = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Store.objects.create(**validated_data)

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Supplier
        fields = "__all__"
        read_only_fields = ('created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Supplier.objects.create(**validated_data)
