from rest_framework.viewsets import ModelViewSet
from .models import WarehouseStock, StoreStock, Product, ProductCategory
from .serializers import WarehouseStockSerializer, StoreStockSerializer, ProductSerializer, ProductCategorySerializer
from .permissions import WarehouseStockPermissions, StoreStockPermissions, ProductCategoryPermissions, ProductPermissions

class BaseViewSet(ModelViewSet):
    """
    A base viewset is created that alters the perform_create method to automatically populate the 
    created_by field with the user requesting the view.
    """
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class ProductCategoryViewSet(BaseViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (ProductCategoryPermissions,)

class WarehouseStockViewSet(BaseViewSet):
    queryset = WarehouseStock.objects.all()
    serializer_class = WarehouseStockSerializer
    permission_classes = (WarehouseStockPermissions,)

class StoreStockViewSet(BaseViewSet):
    queryset = StoreStock.objects.all()
    serializer_class = StoreStockSerializer
    permission_classes = (StoreStockPermissions,)

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermissions,)