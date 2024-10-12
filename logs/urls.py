from django.urls import path
from .views import UserWarehouseStockListView

urlpatterns = [
    path("warehouse-stock/users/<int:pk>/", UserWarehouseStockListView.as_view(), name="warehouse-stock-user-log")
]