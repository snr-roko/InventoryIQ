from rest_framework.viewsets import ModelViewSet
from .models import WarehouseStock, StoreStock, Product
from .serializers import WarehouseStockSerializer, StoreStockSerializer, ProductSeralizer


class BaseViewSet(ModelViewSet):
    """
    A base viewset is created that alters the perform_create method to automatically populate the 
    created_by field with the user requesting the view.
    """
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class WarehouseStockViewSet(BaseViewSet):
    queryset = WarehouseStock.objects.all()
    serializer_class = WarehouseStockSerializer

class StoreStockViewSet(BaseViewSet):
    queryset = StoreStock.objects.all()
    serializer_class = StoreStockSerializer

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer