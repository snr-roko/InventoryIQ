from rest_framework import viewsets
from .models import Warehouse, Store, Supplier
from .serializers import WarehouseSerializer, StoreSerializer, SupplierSerializer
from .permissions import WarehousePermission, StorePermission, SupplierPermission

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (WarehousePermission,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (StorePermission,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (SupplierPermission,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)