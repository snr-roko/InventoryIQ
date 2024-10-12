from django.urls import path
from .views import UserWarehouseStockListView, UserStoreStockListView, UserProductCategoryListView, UsersLogListView

urlpatterns = [
    path("warehouse-stock/users/<int:pk>/", UserWarehouseStockListView.as_view(), name="warehouse-stock-user-log"),
    path("store-stock/users/<int:pk>/", UserStoreStockListView.as_view(), name="store-stock-user-log"),
    path("category/users/<int:pk>/", UserProductCategoryListView.as_view(), name="cateory-user-log"),
    path("users/<int:pk>/", UsersLogListView.as_view(), name="users-log")
]