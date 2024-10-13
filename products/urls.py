from django.urls import path, include
from .views import WarehouseStockViewSet, StoreStockViewSet, ProductViewSet, ProductCategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("warehouse-stocks", WarehouseStockViewSet, basename="warehouse-stocks")
router.register("store-stocks", StoreStockViewSet, basename="store-stocks")
router.register("categories", ProductCategoryViewSet, basename="categories")
router.register("", ProductViewSet, basename="products")


urlpatterns = router.urls