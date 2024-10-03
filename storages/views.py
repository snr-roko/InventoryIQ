from rest_framework.viewsets import ModelViewSet
from .models import Warehouse, Store, Supplier
from .serializers import WarehouseSerializer, StoreSerializer, SupplierSerializer

class BaseViewSet(ModelViewSet):
    def get_serializer_context(self):
        return {'request': self.request}

class WarehouseViewSet(BaseViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class StoreViewSet(BaseViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class SupplierViewSet(BaseViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer