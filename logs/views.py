from rest_framework.generics import ListAPIView
from products.models import WarehouseStock, StoreStock, ProductCategory
from .serializers import WarehouseStockSerializer, StoreStockSerializer
from rest_framework.filters import OrderingFilter
from products.serializers import ProductCategorySerializer
from accounts.serializers import UserListSerializer
from django.contrib.auth import get_user_model
from storages.serializers import WarehouseSerializer, StoreSerializer, SupplierSerializer
from storages.models import Warehouse, Store, Supplier
from sales.models import Order, OrderItem, Customer, StockTransfer
from sales.serializers import OrderItemSerializer, OrderSerializer, CustomerSerializer, StockTransferSerializer
from .permissions import LogsPermissions

class UserWarehouseStockListView(ListAPIView):
    serializer_class = WarehouseStockSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "warehouse", "supplier"]
    ordering = ["stock_code"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return WarehouseStock.objects.filter(created_by=user_id)
    
class UserStoreStockListView(ListAPIView):
    serializer_class = StoreStockSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "store", "supplier"]
    ordering = ["stock_code"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return StoreStock.objects.filter(created_by=user_id) 
    
class UserProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "active"]
    ordering = ["name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return ProductCategory.objects.filter(created_by=user_id)
    
class UsersLogListView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["full_name", "email"]
    ordering = ["full_name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return get_user_model().objects.filter(created_by=user_id)
    
class UserWarehouseLogListView(ListAPIView):
    serializer_class = WarehouseSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "location"]
    ordering = ["name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Warehouse.objects.filter(created_by=user_id)
    
class UserStoreLogListView(ListAPIView):
    serializer_class = StoreSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "location"]
    ordering = ["name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Store.objects.filter(created_by=user_id)


class UserSupplierLogListView(ListAPIView):
    serializer_class = SupplierSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "address"]
    ordering = ["name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Supplier.objects.filter(created_by=user_id)
            
class UserCustomerLogListView(ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "email"]
    ordering = ["name"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Customer.objects.filter(created_by=user_id)

class UserOrderItemLogListView(ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["order", "product", "store", "total_price", "customer", "order_date"]
    ordering = ["order"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return OrderItem.objects.filter(created_by=user_id)

class UserOrderLogListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["order_date", "total_amount", "status", "customer"]
    ordering = ["order_date"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Order.objects.filter(created_by=user_id)
    
class UserStockTransferLogListView(ListAPIView):
    serializer_class = StockTransferSerializer
    permission_classes = (LogsPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["source", "destination", "stock", "date_transferred", "quantity", "status"]
    ordering = ["stock"]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return StockTransfer.objects.filter(created_by=user_id)