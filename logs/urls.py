from django.urls import path
from .views import (UserWarehouseStockListView, UserStoreStockListView, UserProductCategoryListView, UsersLogListView,
                    UserStoreLogListView, UserWarehouseLogListView, UserSupplierLogListView, UserCustomerLogListView, 
                    UserOrderItemLogListView, UserOrderLogListView, UserStockTransferLogListView)

urlpatterns = [
    path("warehouse-stocks/users/<int:pk>/", UserWarehouseStockListView.as_view(), name="warehouse-stock-user-log"),
    path("store-stocks/users/<int:pk>/", UserStoreStockListView.as_view(), name="store-stock-user-log"),
    path("categories/users/<int:pk>/", UserProductCategoryListView.as_view(), name="cateory-user-log"),
    path("users/<int:pk>/", UsersLogListView.as_view(), name="users-log"),
    path("warehouses/users/<int:pk>/", UserWarehouseLogListView.as_view(), name="warehouse-user-log"),
    path("stores/users/<int:pk>/", UserStoreLogListView.as_view(), name="store-user-log"),
    path("suppliers/users/<int:pk>/", UserSupplierLogListView.as_view(), name="supplier-user-log"),
    path("customers/users/<int:pk>/", UserCustomerLogListView.as_view(), name="customer-user-log"),
    path("order-items/users/<int:pk>/", UserOrderItemLogListView.as_view(), name="orderItem-user-log"),
    path("orders/users/<int:pk>/", UserOrderLogListView.as_view(), name="order-user-log"),
    path("stock-transfers/users/<int:pk>/", UserStockTransferLogListView.as_view(), name="stockTransfer-user-log"),    
]