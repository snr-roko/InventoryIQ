from rest_framework import viewsets
from .models import Warehouse, Store, Supplier
from .serializers import WarehouseSerializer, StoreSerializer, SupplierSerializer
from .permissions import WarehousePermission, StorePermission, SupplierPermission
from rest_framework.filters import OrderingFilter

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (WarehousePermission,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "location"]
    ordering = ["name"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (StorePermission,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "location"]
    ordering = ["name"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (SupplierPermission,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "address"]
    ordering = ["name"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)