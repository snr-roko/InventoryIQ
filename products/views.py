from rest_framework.viewsets import ModelViewSet
from .models import WarehouseStock, StoreStock, Product, ProductCategory
from .serializers import WarehouseStockSerializer, StoreStockSerializer, ProductSerializer, ProductCategorySerializer
from .permissions import WarehouseStockPermissions, StoreStockPermissions, ProductCategoryPermissions, ProductPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from storages.models import Warehouse

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

    def list(self, request, *args, **kwargs):
        """
        This seeks to serve a view add on for the warehouse stock view set when additional query parameters are added
        Specifically category, active, and warehouse, supplier parameters
        """
        # Here, we retrieve each parameter
        category_param = request.query_params.get("category")
        active_param = request.query_params.get("active")
        warehouse_param = request.query_params.get("warehouse")
        supplier_params = request.query_params.getlist("supplier")

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

        # The above makes sure that only available query parameters are used to filter the model

        # Then we unpack the details of the filter dictionary.
        # This does the trick since if none of the parameters are available, nothing would be unpacked 
        # And thus the queryset will be the same as the instance queryset attibute
        queryset = WarehouseStock.objects.filter(**filterDict).distinct()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)       

class StoreStockViewSet(BaseViewSet):
    queryset = StoreStock.objects.all()
    serializer_class = StoreStockSerializer
    permission_classes = (StoreStockPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "stock_code", "category", "quantity", "active", "store", "supplier"]
    ordering = ["stock_code"]    

    def list(self, request, *args, **kwargs):
        """
        This seeks to serve a view add on for the store stock view set when additional query parameters are added
        Specifically category, active, and store, supplier parameters
        """
        # Here, we retrieve each parameter
        category_param = request.query_params.get("category")
        active_param = request.query_params.get("active")
        store_param = request.query_params.get("store")
        supplier_params = request.query_params.getlist("supplier")

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

        # The above makes sure that only available query parameters are used to filter the model

        # Then we unpack the details of the filter dictionary.
        # This does the trick since if none of the parameters are available, nothing would be unpacked 
        # And thus the queryset will be the same as the instance queryset attibute
        queryset = StoreStock.objects.filter(**filterDict).distinct()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data) 
          
    def retrieve(self, request, *args, **kwargs):
        """
        This function serves to render barcode query parameters and retrieve an object based on the barcode.
        """
        barcode = request.query_params.get('barcode')
        if barcode:
            queryset = StoreStock.objects.filter(barcode=barcode)
            serializer = self.serializer_class(queryset)
        else:
            serializer = self.serializer_class(self.queryset)
        return Response(serializer.data)

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name", "product_code", "category", "quantity", "active"]
    ordering = ["product_code"]  

    def list(self, request, *args, **kwargs):
        """
        This seeks to serve a view add on for the product view set when additional query parameters are added
        Specifically category and active
        """
        # Here, we retrieve each parameter
        category_param = request.query_params.get("category")
        active_param = request.query_params.get("active")

        # we create a dictionary to unpack into the model
        filterDict = dict()

        if category_param:
            filterDict['category'] = category_param
        if active_param is not None:
            filterDict['active'] = active_param.lower() in ['true', 'yes', '1']

        # The above makes sure that only available query parameters are used to filter the model

        # Then we unpack the details of the filter dictionary.
        # This does the trick since if none of the parameters are available, nothing would be unpacked 
        # And thus the queryset will be the same as the instance queryset attibute
        queryset = Product.objects.filter(**filterDict)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)