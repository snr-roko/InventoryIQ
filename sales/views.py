from rest_framework.viewsets import ModelViewSet
from .models import OrderItem, Order, Customer, StockTransfer
from .serializers import OrderItemSerializer, OrderSerializer, CustomerSerializer, StockTransferSerializer

class BaseViewSet(ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class CustomerViewSet(BaseViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderItemViewSet(BaseViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(BaseViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class StockTransferViewSet(BaseViewSet):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer

