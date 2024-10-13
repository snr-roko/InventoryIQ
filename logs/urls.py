from django.urls import path
from .views import (UserWarehouseStockListView, UserStoreStockListView, UserProductCategoryListView, UsersLogListView,
                    UserStoreLogListView, UserWarehouseLogListView, UserSupplierLogListView)

urlpatterns = [
    path("warehouse-stock/users/<int:pk>/", UserWarehouseStockListView.as_view(), name="warehouse-stock-user-log"),
    path("store-stock/users/<int:pk>/", UserStoreStockListView.as_view(), name="store-stock-user-log"),
    path("category/users/<int:pk>/", UserProductCategoryListView.as_view(), name="cateory-user-log"),
    path("users/<int:pk>/", UsersLogListView.as_view(), name="users-log"),
    path("warehouse/users/<int:pk>/", UserWarehouseLogListView.as_view(), name="warehouse-user-log"),
    path("store/users/<int:pk>/", UserStoreLogListView.as_view(), name="store-user-log"),
    path("supplier/users/<int:pk>/", UserSupplierLogListView.as_view(), name="supplier-user-log"),
]