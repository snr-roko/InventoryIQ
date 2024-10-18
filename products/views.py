from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from .models import WarehouseStock, StoreStock, Product, ProductCategory
from .serializers import WarehouseStockSerializer, StoreStockSerializer, ProductSerializer, ProductCategorySerializer
from .permissions import WarehouseStockPermissions, StoreStockPermissions, ProductCategoryPermissions, ProductPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status

class BaseViewSet(ModelViewSet):
    """
    A base viewset is created that alters the perform_create method to automatically populate the 
    created_by field with the user requesting the view.
    """
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class BarcodeViewSet(RetrieveAPIView):
    serializer_class = StoreStockSerializer
    permission_classes = (StoreStockPermissions,) 

    def retrieve(self, request, *args, **kwargs):
        barcode = self.kwargs['pk']
        try:
            store_stock = StoreStock.objects.get(barcode=barcode)
            serializer = self.serializer_class(store_stock)
            return Response(serializer.data)
        except StoreStock.DoesNotExist:
            return Response(data="Store Stock not found. Barcode does not exist.", status=status.HTTP_404_NOT_FOUND)

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
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "warehouse", "supplier", "low_stock"]
    ordering = ["stock_code"]    

    def get_queryset(self):
        """
        This seeks to serve a view add on for the warehouse stock view set when additional query parameters are added
        Specifically category, active, warehouse, supplier and low stock parameters
        """
        # Here, we retrieve each parameter
        category_param = self.request.query_params.get("category", None)
        active_param = self.request.query_params.get("active", None)
        warehouse_param = self.request.query_params.get("warehouse", None)
        supplier_params = self.request.query_params.getlist("supplier", None)
        low_stock_param = self.request.query_params.get("low-stock", None)

        # we create a dictionary to unpack into the model
        filterDict = dict()

        if category_param:
            filterDict['category'] = category_param
        if active_param is not None:
            filterDict['active'] = active_param.lower() in ['true', 'yes', '1']
        if warehouse_param:
            filterDict['warehouse'] = warehouse_param
        if supplier_params:
            filterDict['supplier__in'] = supplier_params
        if low_stock_param is not None:
            filterDict["low_stock"] = low_stock_param.lower() in ['true', 'yes', '1']

        # The above makes sure that only available query parameters are used to filter the model

        # Then we unpack the details of the filter dictionary.
        # This does the trick since if none of the parameters are available, nothing would be unpacked 
        # And thus the queryset will be the same as the instance queryset attibute
        queryset = super().get_queryset()
        if filterDict:
            queryset = WarehouseStock.objects.filter(**filterDict).distinct()
        return queryset       

class StoreStockViewSet(BaseViewSet):
    queryset = StoreStock.objects.all()
    serializer_class = StoreStockSerializer
    permission_classes = (StoreStockPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "store", "supplier", "low_stock", "price"]
    ordering = ["stock_code"]    

    def get_queryset(self):
        """
        This seeks to serve a view add on for the store stock view set when additional query parameters are added
        Specifically category, active, and store, supplier and low stock parameters
        """
        # Here, we retrieve each parameter
        category_param = self.request.query_params.get("category")
        active_param = self.request.query_params.get("active")
        store_param = self.request.query_params.get("store")
        supplier_params = self.request.query_params.getlist("supplier")
        low_stock_param = self.request.query_params.get("low-stock")

        # we create a dictionary to unpack into the model
        filterDict = dict()

        if category_param:
            filterDict['category'] = category_param
        if active_param is not None:
            filterDict['active'] = active_param.lower() in ['true', 'yes', '1']
        if store_param:
            filterDict['store'] = store_param
        if supplier_params:
            filterDict['supplier__in'] = supplier_params
        if low_stock_param is not None:
            filterDict["low_stock"] = low_stock_param.lower() in ['true', 'yes', '1']            

        # The above makes sure that only available query parameters are used to filter the model

        # Then we unpack the details of the filter dictionary.
        # This does the trick since if none of the parameters are available, nothing would be unpacked 
        # And thus the queryset will be the same as the instance queryset attibute
        queryset = super().get_queryset()
        if filterDict:
            queryset = StoreStock.objects.filter(**filterDict).distinct()

        return queryset

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "product_code", "category", "quantity", "active"]
    ordering = ["product_code"]  

    def get_queryset(self):
        queryset = super().get_queryset()
        """
        This seeks to serve a view add on for the product view set when additional query parameters are added
        Specifically category, active and low stock parameters
        """
        # Here, we retrieve each parameter
        category_param = self.request.query_params.get("category")
        active_param = self.request.query_params.get("active")
        low_stock_param = self.request.query_params.get("low-stock")

        # we create a dictionary to unpack into the model
        filterDict = dict()

        if category_param:
            filterDict['category'] = category_param
        if active_param is not None:
            filterDict['active'] = active_param.lower() in ['true', 'yes', '1']
        if low_stock_param is not None:
            filterDict["low_stock"] = low_stock_param.lower() in ['true', 'yes', '1']     

        # The above makes sure that only available query parameters are used to filter the model

        # Then we unpack the details of the filter dictionary.
        # This does the trick since if none of the parameters are available, nothing would be unpacked 
        # And thus the queryset will be the same as the instance queryset attibute
        if filterDict:
            queryset = Product.objects.filter(**filterDict)
        return queryset