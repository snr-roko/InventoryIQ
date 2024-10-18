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

class StoreStockTests(TestCase):
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

        # 5 Stores objects created
        Store.objects.bulk_create([
            Store(id=1, name="Ejisu A", location ="Ejisu"), 
            Store(id=2, name="Ejisu B", location="Ejisu"), 
            Store(id=3, name="Tema A", location="Tema"),
            Store(id=4, name="Tema B", location="Tema"), 
            Store(id=5, name="Kasoa A", location="Kasoa")
        ])

        ProductCategory.objects.bulk_create([
            ProductCategory(id=1, name="Phones"),
            ProductCategory(id=2, name="Laptops"),
            ProductCategory(id=3, name="Monitors"),
            ProductCategory(id=4, name="System Units")
        ])

        StoreStock.objects.bulk_create([
            StoreStock(id=1, name="Samsang S21", stock_code="SAMSS2112256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), barcode="2723747937124", price=799.00),
            StoreStock(id=2, name="Samsung S22", stock_code="SAMSS2216256BLUE", quantity=60, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=999.00),
            StoreStock(id=3, name="Samsung S21", stock_code="SAMSS2112256WHITE", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=799.00),
            StoreStock(id=4, name="Samsung S23", stock_code="SAMSS2312256RED", quantity=30, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=1100.00),
            StoreStock(id=5, name="Samsung S24", stock_code="SAMSS2412256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=1200.00)
        ])

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)        
    
    def test_storestocks_list(self):
        """
        Testing all stores stocks get endpoint
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
    
    def test_storestocks_list_denied(self):
        """
        Testing for denial of access for non permitted user
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_storestocks_detail(self):
        """
        Testing for single store stock resource endpoint
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-detail", args=[1])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))
        self.assertEqual(response.data['stock_code'], "SAMSS2112256RED")

    def test_storestocks_detail_barcode(self):
        """
        Testing for retrieval of stock resource using barcode
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("barcode", args=['2723747937124'])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))
        self.assertEqual(response.data['stock_code'], "SAMSS2112256RED")
        

    def test_storestocks_detail_denied(self):
        """
        Testing for denial of access for non permitted user
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-detail", args=[1])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_storestocks_create(self):
        """
        Testing for creation of new store stock
        """
        new_store_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "store": 1,
            "price": 2000.00
        }
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-list")
        response = self.api.post(uri, new_store_stock)
        all_store_stocks = StoreStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_store_stocks, 6)

    def test_storestocks_create_denied(self):
        """
        Testing for creation of new store stock by a unpermitted user
        """
        new_store_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "store": 1,
            "price": 2000.00
        }
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-list")
        response = self.api.post(uri, new_store_stock)
        all_store_stocks = StoreStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_store_stocks, 5)

    def test_storestocks_update(self):
        """
        Testing for update of store stock
        """
        update_store_stock = {
            "name": "Samsung S21",
            "reorder_level": 30, 
            "store": 3
        }
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-detail", args=[1])
        response = self.api.patch(uri, update_store_stock)
        all_store_stocks = StoreStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(all_store_stocks, 5)
        self.assertEqual(response.data['name'], update_store_stock["name"])
        self.assertEqual(response.data['reorder_level'], update_store_stock["reorder_level"])
        self.assertEqual(response.data['store'], update_store_stock["store"])

    def test_storestocks_update_denied(self):
        """
        Testing for update of store stock by an unpermitted user
        """
        update_store_stock = {
            "name": "Samsung S21",
            "reorder_level": 30, 
            "store": 3
        }
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-detail", args=[1])
        response = self.api.patch(uri, update_store_stock)
        all_store_stocks = StoreStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_store_stocks, 5)

    def test_storestocks_delete(self):
        """
        Testing for deletion of a single store stock resource endpoint
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-detail", args=[1])
        response = self.api.delete(uri)
        all_store_stocks = StoreStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(all_store_stocks, 4)

    def test_storestocks_delete_denied(self):
        """
        Testing for deletion of a single store stock resource endpoint by an unpermitted user
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-detail", args=[1])
        response = self.api.delete(uri)
        all_store_stocks = StoreStock.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_store_stocks, 5)

    def test_storestocks_create_product_signal(self):
        """
        Testing for creation of products when store stocks are created
        """        
        new_store_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "store": 1,
            "price": 2000.00
        }
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("store-stocks-list")
        response = self.api.post(uri, new_store_stock)
        all_products = Product.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_products, 1)    

    def test_warehousestocks_storestocks_create_product_signal(self):
        """
        Testing for quantity calcuation of products when both warehousestocks and storestocks are created and deleted
        Also testing for get all products endpoint
        """
        new_warehouse_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":250,
            "reorder_level":30,
            "category":2, 
            "warehouse": 1
        }
        new_store_stock = {
            "name":"HP Pavilion",
            "stock_code":"HPSSD500RAM32SILVER",
            "quantity":150,
            "reorder_level":30,
            "category":2, 
            "store": 1,
            "price": 2000.00
        }        
        token = self.get_token_for_user(self.manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouse-stocks-list")
        url = reverse("store-stocks-list")
        # create a new warehouse stock
        warehouse_response = self.api.post(uri, new_warehouse_stock)
        warehouse_id = warehouse_response.data['id']
        
        # create a new store stock
        store_response = self.api.post(url, new_store_stock)
        store_id = store_response.data['id']

        # retrieve all products
        # expecting one product since both warehouse stock and stock have the same stock_code
        product_uri = reverse("products-list")
        response = self.api.get(product_uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

        # retrieve the id for retrieval api request usage
        id = response.data['results'][0]['id']
        product_resource_uri = reverse("products-detail", args=[id])
        resource_response = self.api.get(product_resource_uri)
        self.assertTrue(isinstance(resource_response.data, dict))
        self.assertEqual(resource_response.status_code, status.HTTP_200_OK)

        # making sure the product model added both warehouse stock and store stock quantities together
        self.assertEqual(resource_response.data['quantity'], 400)


        # deleting warehousestock
        warehouse_url_delete = reverse("warehouse-stocks-detail", args=[warehouse_id])
        self.api.delete(warehouse_url_delete)
        
        # retrieve product again
        new_response_after_delete = self.api.get(product_uri)
        self.assertEqual(new_response_after_delete.status_code, status.HTTP_200_OK)
        self.assertEqual(len(new_response_after_delete.data['results']), 1)

        # retrieve single product
        resource_response = self.api.get(product_resource_uri)
        self.assertTrue(isinstance(resource_response.data, dict))
        self.assertEqual(resource_response.status_code, status.HTTP_200_OK)

        # making sure the product model now has only the store quantity
        self.assertEqual(resource_response.data['quantity'], 150)

        # delete store stock as well
        store_url_delete = reverse("store-stocks-detail", args=[store_id])
        self.api.delete(store_url_delete)
        
        # retrieve product again
        another_response = self.api.get(product_uri)
        self.assertEqual(another_response.status_code, status.HTTP_200_OK)
        # making sure product is not deleted when both warehouse stocks and store stocks are deleted
        self.assertEqual(len(another_response.data['results']), 1)

        # retrieve single product
        new_resource_response = self.api.get(product_resource_uri)
        self.assertTrue(isinstance(new_resource_response.data, dict))
        self.assertEqual(new_resource_response.status_code, status.HTTP_200_OK)

        # making sure the product model now has 0 quantity and making sure product was deactivated
        self.assertEqual(new_resource_response.data['active'], False)
        self.assertEqual(new_resource_response.data['quantity'], 0)
        

    
