from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Warehouse, Store, Supplier
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class WarehouseTests(TestCase):
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
    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_warehouse_list_accepted(self):
        """
        This tests the validity of the warehouse list endpoint
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

    def test_warehouse_list_denial(self):
        """
        This checks whether a store manager will be denied access to view warehouses
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            
    def test_warehouse_object(self):
        """
        This checks a warehouse retrieval endpoint success
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-detail", args=[1])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['name'], "Ejisu A")

    def test_warehouse_creation(self):
        """
        This checks for a warehouse creation success
        """        
        new_warehouse = {
            "name": "Kasoa B",
            "location": "Kasoa"
        }
        token = self.get_token_for_user(self.manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-list")
        response = self.api.post(uri, new_warehouse)
        all_warehouses = Warehouse.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_warehouses, 6)
    def test_warehouse_creation_denial(self):
        """
        This checks whether a warahouse manager will be denied a warehouse creation action
        """
        new_warehouse = {
            "name": "Kasoa C",
            "location": "Kasoa"
        }
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-list")
        response = self.api.post(uri, new_warehouse)
        all_warehouses = Warehouse.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_warehouses, 5)        

    def test_warehouse_update(self):
        """
        This checks the update warehouse endpoint
        """
        new_warehouse = {
            "phone": "0545454545"
        }
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-detail", args=[1])
        response = self.api.patch(uri, new_warehouse)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone'], new_warehouse["phone"])

    def test_warehouse_delete(self):
        """
        This checks the delete warehouse endpoint
        """
        token = self.get_token_for_user(self.manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-detail", args=[1])
        response = self.api.delete(uri)
        all_warehouses = Warehouse.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(all_warehouses, 4)
        self.assertFalse(Warehouse.objects.filter(name="Ejisu A").exists())

    def test_warehouse_delete_denial(self):
        """
        This checks the delete warehouse endpoint permissions
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("warehouses-detail", args=[1])
        response = self.api.delete(uri)
        all_warehouses = Warehouse.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_warehouses, 5)
        self.assertTrue(Warehouse.objects.filter(name="Ejisu A").exists())

class StoreTests(TestCase):
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
        # 5 store objects created
        Store.objects.bulk_create([
            Store(id=1, name="Ejisu A", location ="Ejisu"), 
            Store(id=2, name="Ejisu B", location="Ejisu"), 
            Store(id=3, name="Tema A", location="Tema"),
            Store(id=4, name="Tema B", location="Tema"), 
            Store(id=5, name="Kasoa A", location="Kasoa")
        ])
    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_stores_list_accepted(self):
        """
        This tests the validity of the stores list endpoint
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)

    def test_stores_list_denial(self):
        """
        This checks whether a warehouse manager will be denied access to view stores
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-list")
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            
    def test_store_object(self):
        """
        This checks a store retrieval endpoint success
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-detail", args=[1])
        response = self.api.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['name'], "Ejisu A")

    def test_store_creation(self):
        """
        This checks for a store creation success
        """        
        new_store = {
            "name": "Kasoa B",
            "location": "Kasoa"
        }
        token = self.get_token_for_user(self.manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-list")
        response = self.api.post(uri, new_store)
        all_stores = Store.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_stores, 6)
    def test_store_creation_denial(self):
        """
        This checks whether a store manager will be denied a store creation action
        """
        new_store = {
            "name": "Kasoa C",
            "location": "Kasoa"
        }
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-list")
        response = self.api.post(uri, new_store)
        all_stores = Store.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_stores, 5)        

    def test_store_update(self):
        """
        This checks the update store endpoint
        """
        new_store = {
            "phone": "0545454545"
        }
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-detail", args=[1])
        response = self.api.patch(uri, new_store)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone'], new_store["phone"])

    def test_store_delete(self):
        """
        This checks the delete store endpoint
        """
        token = self.get_token_for_user(self.manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-detail", args=[1])
        response = self.api.delete(uri)
        all_stores = Store.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(all_stores, 4)
        self.assertFalse(Store.objects.filter(name="Ejisu A").exists())

    def test_store_delete_denial(self):
        """
        This checks the delete store endpoint permissions
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("stores-detail", args=[1])
        response = self.api.delete(uri)
        all_stores = Store.objects.count()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_stores, 5)
        self.assertTrue(Store.objects.filter(name="Ejisu A").exists())
