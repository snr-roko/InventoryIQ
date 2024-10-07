from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, OrderItemViewSet, OrderViewSet, StockTransferViewSet

router = DefaultRouter()

router.register("customers", CustomerViewSet, basename="customers")
router.register("orders", OrderViewSet, basename="orders")
router.register("order-items", OrderItemViewSet, basename="order-items")
router.register("stock-transfers", StockTransferViewSet, basename="stock-transfers")

urlpatterns = router.urls