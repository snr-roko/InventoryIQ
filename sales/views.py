from rest_framework.viewsets import ModelViewSet
from .models import OrderItem, Order, Customer, StockTransfer
from .serializers import OrderItemSerializer, OrderSerializer, CustomerSerializer, StockTransferSerializer
from .permissions import CustomerPermissions, OrderItemPermissions, OrderPermissions, StockTransferPermissions
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from django.db.models import Q

def parse_dates(date_str):
    try:
        return parse_date(date_str)
    except ValueError:
        return None

class BaseViewSet(ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class CustomerViewSet(BaseViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (CustomerPermissions,)

class OrderItemViewSet(BaseViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (OrderItemPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ("customer", "order_date", "price", "total_price", "order", "product", "store")
    ordering = ("order_date",)

    def get_queryset(self):
        """
        Overriding the get queryset method to add filtering using query parmaters
        """
        customer_id = self.request.query_params.get("customer")
        order_date_from = self.request.query_params.get("date-from")
        order_date_to = self.request.query_params.get("date-to")
        order_id = self.request.query_params.get("order")
        product_id = self.request.query_params.get("product")
        store_id = self.request.query_params.get("store")

        filter_kwargs = dict()
        date_filter = Q()

        if customer_id:
            filter_kwargs['customer'] = customer_id
        if order_id:
            filter_kwargs['order'] = order_id
        if product_id:
            filter_kwargs['product'] = product_id
        if store_id:
            filter_kwargs['store'] = store_id

        if order_date_from:
            parse_date_from = parse_dates(order_date_from)
            if parse_date_from:
                date_filter &= Q(order_date__gte=parse_date_from)
        if order_date_to:
            parse_date_to = parse_dates(order_date_to)
            if parse_date_to:
                date_filter &= Q(order_date__lte=parse_date_to)
        
        queryset = super().get_queryset()

        if filter_kwargs or date_filter:
            queryset = OrderItem.objects.filter(**filter_kwargs).filter(date_filter)

        return queryset
        

class OrderViewSet(BaseViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ("order_date", "total_amount", "status")
    ordering = ("order_date",)

    def get_queryset(self):
        """
        The get_queryset method is overridden to add filters through query parameters to the url.
        A dictionary is unpacked into the model to retrieve data based on the query parameters present.
        """
        queryset = super().get_queryset()
        customer_id = request.query_params.get("customer")
        order_date_from = request.query_params.get("date-from")
        order_date_to = request.query_params.get("date-to")
        status = request.query_params.get("status")

        filter_kwargs = dict()
        date_filter = Q()

        if customer_id:
            filter_kwargs['customer'] = customer_id
        if status:
            filter_kwargs["status"] = status

        if order_date_from:
            parsed_order_date_from = parse_dates(order_date_from)
            if parsed_order_date_from:
                date_filter &= Q(order_date__gte=parsed_order_date_from)
        if order_date_to:
            parsed_order_date_to = parse_dates(order_date_to)
            if parsed_order_date_to:
                date_filter &= Q(order_date__lte=parsed_order_date_to)

        if filter_kwargs or date_filter:
            queryset = Order.objects.filter(**filter_kwargs).filter(date_filter)
        
        return queryset

class StockTransferViewSet(BaseViewSet):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer
    permission_classes = (StockTransferPermissions,)
    filter_backends = (OrderingFilter,)
    ordering_fields = ("source", "destination", "date_transferred", "stock", "quantity", "status")
    ordering = ("date_transferred",)

    def get_queryset(self):
        queryset = super().get_queryset()

        warehouse_id = request.query_params.get("warehouse")
        store_id = request.query_params.get("store")
        date_from = request.query_params.get("date-from")
        date_to = request.query_params.get("date-to")
        warehousestock_id = request.query_params.get("stock")
        status = request.query_params.get("status")

        filter_kwargs = dict()
        date_filter = Q()

        if warehouse_id:
            filter_kwargs['source'] = warehouse_id
        if store_id:
            filter_kwargs['destination'] = store_id
        if warehousestock_id:
            filter_kwargs["stock"] = warehousestock_id
        if status:
            filter_kwargs['status'] = status

        if date_from:
            parsed_date_from = parse_dates(date_from)
            if parsed_date_from:
                date_filter = date_filter & Q(date_transferred__gte=parsed_date_from)

        if date_to:
            parsed_date_to = parse_dates(date_to)
            if parsed_date_to:
                date_filter = date_filter & Q(date_transferred__lte=parsed_date_to)
        
        if filter_kwargs or date_filter:
            queryset = StockTransfer.objects.filter(**filter_kwargs).filter(date_filter)

        return queryset
