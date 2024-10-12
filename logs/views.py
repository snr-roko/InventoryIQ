from rest_framework.generics import ListAPIView
from products.models import WarehouseStock, StoreStock, ProductCategory
from .serializers import WarehouseStockSerializer, StoreStockSerializer
from rest_framework.filters import OrderingFilter
from products.serializers import ProductCategorySerializer
from accounts.serializers import UserListSerializer
from django.contrib.auth import get_user_model

class UserWarehouseStockListView(ListAPIView):
    serializer_class = WarehouseStockSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "warehouse", "supplier"]
    ordering = ["stock_code"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return WarehouseStock.objects.filter(created_by=user_id)
    
class UserStoreStockListView(ListAPIView):
    serializer_class = StoreStockSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "store", "supplier"]
    ordering = ["stock_code"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return StoreStock.objects.filter(created_by=user_id) 
    
class UserProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "active"]
    ordering = ["name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return ProductCategory.objects.filter(created_by=user_id)
    
class UsersLogListView(ListAPIView):
    serializer_class = UserListSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ["full_name", "email"]
    ordering = ["full_name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return get_user_model().objects.filter(created_by=user_id)