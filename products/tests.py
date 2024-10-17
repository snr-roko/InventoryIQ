from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ProductCategory, WarehouseStock, StoreStock, Product
from django.urls import reverse
from rest_framework import status

User = get_user_model()

class WarehouseStockTests(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.manager_user = User.objects.create_user(
            username = "managertestuser",
            email = "managertestuser@test.com",
            password = "secretpassword",
            role = "MANAGER"
        )
        self.staff_user = User.objects.create_user(
            username = "stafftestuser",
            email = "stafftestuser@test.com",
            password = "secretpassword",
            role = "STAFF"
        )
        self.warehouse_manager_user = User.objects.create_user(
            username = "warehousemanagertestuser",
            email = "warehousemanagertestuser@test.com",
            password = "secretpassword",
            role = "WAREHOUSE_MANAGER"
        )
        self.warehouse_staff_user = User.objects.create_user(
            username = "warehousestafftestuser",
            email = "warehousestafftestuser@test.com",
            password = "secretpassword",
            role = "WAREHOUSE_STAFF"
        )
        self.store_manager_user = User.objects.create_user(
            username = "storemanagertestuser",
            email = "storemanagertestuser@test.com",
            password = "secretpassword",
            role = "STORE_MANAGER"
        )
        self.store_staff_user = User.objects.create_user(
            username = "storestafftestuser",
            email = "storestafftestuser@test.com",
            password = "secretpassword",
            role = "STORE_STAFF",
        )

        ProductCategory.objects.bulk_create([
            ProductCategory(id=1, name="Phones"),
            ProductCategory(id=2, name="Laptops"),
            ProductCategory(id=3, name="Monitors"),
            ProductCategory(id=4, name="System Units")
        ])

        WarehouseStock.objects.bulk_create([
            WarehouseStock(id=1, name="Samsung S21", stock_code="SAMSS2112256RED", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            WarehouseStock(id=2, name="Samsung S22", stock_code="SAMSS2216256BLUE", quantity=70, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            WarehouseStock(id=3, name="Samsung S21", stock_code="SAMSS2112256WHITE", quantity=90, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            WarehouseStock(id=4, name="Samsung S23", stock_code="SAMSS2312256RED", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            WarehouseStock(id=5, name="Samsung S24", stock_code="SAMSS2412256RED", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones"))
        ])

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)        
    
    def test_warehousestocks_list(self):
        """
        Testing all warehouse stocks get endpoint
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-list")
        response = self.api.get(uri)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
    