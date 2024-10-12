from rest_framework.viewsets import ModelViewSet
from .models import OrderItem, Order, Customer, StockTransfer
from .serializers import OrderItemSerializer, OrderSerializer, CustomerSerializer, StockTransferSerializer
from .permissions import CustomerPermissions, OrderItemPermissions, OrderPermissions, StockTransferPermissions

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

class OrderViewSet(BaseViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderPermissions,)

class StockTransferViewSet(BaseViewSet):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer
    permission_classes = (StockTransferPermissions,)

