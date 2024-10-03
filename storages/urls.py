from django.urls import path
from .views import WarehouseViewSet, StoreViewSet, SupplierViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("warehouses", WarehouseViewSet, basename="warehouses")
router.register("stores", StoreViewSet, basename="stores")
router.register("suppliers", SupplierViewSet, basename="suppliers")

urlpatterns = router.urls