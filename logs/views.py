from rest_framework.generics import ListAPIView
from products.models import WarehouseStock
from .serializers import WarehouseStockSerializer

class UserWarehouseStockListView(ListAPIView):
    serializer_class = WarehouseStockSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return WarehouseStock.objects.filter(created_by=user_id)