from django.urls import path, include
from .views import WarehouseStockViewSet, StoreStockViewSet, ProductViewSet, ProductCategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("warehouses", WarehouseStockViewSet, basename="warehouses")
router.register("stores", StoreStockViewSet, basename="stores")
router.register("categories", ProductCategoryViewSet, basename="categories")
router.register("", ProductViewSet, basename="products")


urlpatterns = router.urls