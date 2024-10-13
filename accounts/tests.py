from django.test import TestCase
from .models import UserProfile
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.manager_user = User.objects.create(
            username = "managertestuser",
            email = "managertestuser@test.com",
            password = "secretpassword",
            role = "MANAGER"
        )
        self.staff_user = User.objects.create(
            username = "stafftestuser",
            email = "stafftestuser@test.com",
            password = "secretpassword",
            role = "STAFF"
        )
        self.warehouse_manager_user = User.objects.create(
            username = "warehousemanagertestuser",
            email = "warehousemanagertestuser@test.com",
            password = "secretpassword",
            role = "WAREHOUSE_MANAGER"
        )
        self.warehouse_staff_user = User.objects.create(
            username = "warehousestafftestuser",
            email = "warehousestafftestuser@test.com",
            password = "secretpassword",
            role = "WAREHOUSE_STAFF"
        )
        self.store_manager_user = User.objects.create(
            username = "storemanagertestuser",
            email = "storemanagertestuser@test.com",
            password = "secretpassword",
            role = "STORE_MANAGER"
        )
        self.store_staff_user = User.objects.create(
            username = "storestafftestuser",
            email = "storestafftestuser@test.com",
            password = "secretpassword",
            role = "STORE_STAFF",
        )

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_manager_registering(self):
        """
        Testing for whether a manager can register a staff
        """
        staff_data = {
            "username" : "staff2testuser",
            "email" : "staff2testuser@test.com",
            "password" : "secretpassword",
            "confirm_password" : "secretpassword",
            "role" : "STAFF",
            "full_name": "staff2",
            "phone_number": "0545454455"            
        }
        token = self.get_token_for_user(self.manager_user)
        uri = reverse("register")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")    
        response = self.client.post(uri, staff_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], "staff2testuser")
    
    def test_store_staff_registering(self):
        """
        Checking for whether a store staff will be declined when registering a warehouse manager
        """
        staff_data = {
            "username" : "warehousemanager2testuser",
            "email" : "warehousemanager2testuser@test.com",
            "password" : "secretpassword",
            "confirm_password" : "secretpassword",
            "role" : "WAREHOUSE_MANAGER",
            "full_name": "warehousemanager2",
            "phone_number": "0545454212"
        }
        token = self.get_token_for_user(self.store_staff_user)
        uri = reverse("register")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.post(uri, staff_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_users_list_by_warehouse_manager(self):
        """
        checking for whether users list endpoint works properly and filters properly
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("users")
        response = self.client.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 6)

    def test_users_list_by_warehouse_staff(self):
        """
        Checking whether users list endpoint works properly and filters properly
        """
        token = self.get_token_for_user(self.warehouse_staff_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("users")
        response = self.client.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_profile_users_signal(self):
        """
        checking whether profiles get created automatically upon user creations
        """
        token = self.get_token_for_user(self.manager_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("profile")
        response = self.client.get(uri)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], self.manager_user.email)

    def test_profile_update(self):
        """
        checking whether profile update endpoint is working properly
        """
        bio_data = {
            "bio": "This is the Warehouse Manager"
        }
        token = self.get_token_for_user(self.manager_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        uri = reverse("profile-update")
        response = self.client.put(uri, bio_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], bio_data["bio"])


