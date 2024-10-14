from rest_framework.viewsets import ModelViewSet
from .models import WarehouseStock, StoreStock, Product, ProductCategory
from .serializers import WarehouseStockSerializer, StoreStockSerializer, ProductSerializer, ProductCategorySerializer
from .permissions import WarehouseStockPermissions, StoreStockPermissions, ProductCategoryPermissions, ProductPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

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
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "active"]
    ordering = ["name"]    

class WarehouseStockViewSet(BaseViewSet):
    queryset = WarehouseStock.objects.all()
    serializer_class = WarehouseStockSerializer
    permission_classes = (WarehouseStockPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "warehouse", "supplier"]
    ordering = ["stock_code"]    

    def retrieve(self, request, *args, **kwargs):
        barcode = request.query_params.get('barcode')
        if barcode:
            queryset = WarehouseStock.objects.filter(barcode=barcode)
            serializer = self.serializer_class(queryset)
        else:
            serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer)

class StoreStockViewSet(BaseViewSet):
    queryset = StoreStock.objects.all()
    serializer_class = StoreStockSerializer
    permission_classes = (StoreStockPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "store", "supplier"]
    ordering = ["stock_code"]    

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "product_code", "category", "quantity", "active"]
    ordering = ["product_code"]  