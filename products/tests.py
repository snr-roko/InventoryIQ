from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ProductCategory, WarehouseStock, StoreStock, Product
from django.urls import reverse
from rest_framework import status
from storages.models import Warehouse, Store

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

                # 5 warehouse objects created
        Warehouse.objects.bulk_create([
            Warehouse(id=1, name="Ejisu A", location ="Ejisu"), 
            Warehouse(id=2, name="Ejisu B", location="Ejisu"), 
            Warehouse(id=3, name="Tema A", location="Tema"),
            Warehouse(id=4, name="Tema B", location="Tema"), 
            Warehouse(id=5, name="Kasoa A", location="Kasoa")
        ])

        ProductCategory.objects.bulk_create([
            ProductCategory(id=1, name="Phones"),
            ProductCategory(id=2, name="Laptops"),
            ProductCategory(id=3, name="Monitors"),
            ProductCategory(id=4, name="System Units")
        ])

        WarehouseStock.objects.bulk_create([
            WarehouseStock(id=1, name="Samsang S21", stock_code="SAMSS2112256RED", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
    
    def test_warehousestocks_list_denied(self):
        """
        Testing for denial of access for non permitted user
        """
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_warehousestocks_detail(self):
        """
        Testing for single warehouse stock resource endpoint
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-detail", args=[1])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))
        self.assertEqual(response.data['stock_code'], "SAMSS2112256RED")

    def test_warehousestocks_detail_denied(self):
        """
        Testing for denial of access for non permitted user
        """
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-detail", args=[1])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_warehousestocks_create(self):
        """
        Testing for creation of new warehouse stock
        """
        new_warehouse_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "warehouse": 1
        }
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-list")
        response = self.api.post(uri, new_warehouse_stock)
        all_warehouse_stocks = WarehouseStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_warehouse_stocks, 6)
    def test_warehousestocks_create_denied(self):
        """
        Testing for creation of new warehouse stock by a unpermitted user
        """
        new_warehouse_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "warehouse": 1
        }
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-list")
        response = self.api.post(uri, new_warehouse_stock)
        all_warehouse_stocks = WarehouseStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_warehouse_stocks, 5)
    def test_warehousestocks_update(self):
        """
        Testing for update of warehouse stock
        """
        update_warehouse_stock = {
            "name": "Samsung S21",
            "reorder_level": 30, 
            "warehouse": 3
        }
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-detail", args=[1])
        response = self.api.patch(uri, update_warehouse_stock)
        all_warehouse_stocks = WarehouseStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(all_warehouse_stocks, 5)
        self.assertEqual(response.data['name'], update_warehouse_stock["name"])
        self.assertEqual(response.data['reorder_level'], update_warehouse_stock["reorder_level"])
        self.assertEqual(response.data['warehouse'], update_warehouse_stock["warehouse"])
    def test_warehousestocks_update_denied(self):
        """
        Testing for update of warehouse stock by a unpermitted user
        """
        update_warehouse_stock = {
            "name": "Samsung S21",
            "reorder_level": 30, 
            "warehouse": 3
        }
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-detail", args=[1])
        response = self.api.patch(uri, update_warehouse_stock)
        all_warehouse_stocks = WarehouseStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_warehouse_stocks, 5)

    def test_warehousestocks_delete(self):
        """
        Testing for deletion of a single warehouse stock resource endpoint
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-detail", args=[1])
        response = self.api.delete(uri)
        all_warehouse_stocks = WarehouseStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(all_warehouse_stocks, 4)

    def test_warehousestocks_delete_denied(self):
        """
        Testing for deletion of a single warehouse stock resource endpoint by an unpermitted user
        """
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-detail", args=[1])
        response = self.api.delete(uri)
        all_warehouse_stocks = WarehouseStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_warehouse_stocks, 5)

    def test_warehousestocks_create_product_signal(self):
        """
        Testing for creation of products when warehouse stocks are created
        """        
        new_warehouse_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "warehouse": 1
        }
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-list")
        response = self.api.post(uri, new_warehouse_stock)
        all_products = Product.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_products, 1)    
    
