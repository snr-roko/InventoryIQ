from django.urls import path
from .views import (UserWarehouseStockListView, UserStoreStockListView, UserProductCategoryListView, UsersLogListView,
                    UserStoreLogListView, UserWarehouseLogListView, UserSupplierLogListView, UserCustomerLogListView, 
                    UserOrderItemLogListView, UserOrderLogListView, UserStockTransferLogListView)

urlpatterns = [
    path("users/<int:pk>/warehouse-stocks/", UserWarehouseStockListView.as_view(), name="warehouse-stock-user-log"),
    path("users/<int:pk>/store-stocks/", UserStoreStockListView.as_view(), name="store-stock-user-log"),
    path("users/<int:pk>/categories/", UserProductCategoryListView.as_view(), name="cateory-user-log"),
    path("users/<int:pk>/users/", UsersLogListView.as_view(), name="users-log"),
    path("users/<int:pk>/warehouses/", UserWarehouseLogListView.as_view(), name="warehouse-user-log"),
    path("users/<int:pk>/stores/", UserStoreLogListView.as_view(), name="store-user-log"),
    path("users/<int:pk>/suppliers/", UserSupplierLogListView.as_view(), name="supplier-user-log"),
    path("users/<int:pk>/customers/", UserCustomerLogListView.as_view(), name="customer-user-log"),
    path("users/<int:pk>/order-items/", UserOrderItemLogListView.as_view(), name="orderItem-user-log"),
    path("users/<int:pk>/orders/", UserOrderLogListView.as_view(), name="order-user-log"),
    path("users/<int:pk>/stock-transfers/", UserStockTransferLogListView.as_view(), name="stockTransfer-user-log"),    
]