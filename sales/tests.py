from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Order, OrderItem, StockTransfer
from products.models import ProductCategory, StoreStock

User = get_user_model()

class OrderItems_OrdersTests(TestCase):
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

        StoreStock.objects.bulk_create([
            StoreStock(id=1, name="Samsang S21", stock_code="SAMSS2112256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), barcode="2723747937124"),
            StoreStock(id=2, name="Samsung S22", stock_code="SAMSS2216256BLUE", quantity=60, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            StoreStock(id=3, name="Samsung S21", stock_code="SAMSS2112256WHITE", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            StoreStock(id=4, name="Samsung S23", stock_code="SAMSS2312256RED", quantity=30, reorder_level=10, category=ProductCategory(id=1, name="Phones")),
            StoreStock(id=5, name="Samsung S24", stock_code="SAMSS2412256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"))
        ])
        Order.objects.bulk_create([
            Order(id=1, status='PENDING'),
            Order(id=2, status='PENDING'),
            Order(id=3, status='PENDING'),
            Order(id=4, status='PENDING'),
        ])

        OrderItem.objects.bulk_create([
            OrderItem(price=799.00, quantity=3, total_price=2397.00, order=Order(id=1, status='PENDING'),
                      product= StoreStock(id=1, name="Samsang S21", stock_code="SAMSS2112256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), barcode="2723747937124")
                      ),
            OrderItem(price=899.00, quantity=6, total_price=5394.00, order=Order(id=1, status='PENDING'),
                      product=StoreStock(id=2, name="Samsung S22", stock_code="SAMSS2216256BLUE", quantity=60, reorder_level=10, category=ProductCategory(id=1, name="Phones"))),
            OrderItem(price=1000.00, quantity=10, total_price=10000.00, order=Order(id=2, status='PENDING'),
                     product=StoreStock(id=4, name="Samsung S23", stock_code="SAMSS2312256RED", quantity=30, reorder_level=10, category=ProductCategory(id=1, name="Phones"))
),
            OrderItem(price=1200.00, quantity=5, total_price=6000.00, order=Order(id=2, status='PENDING'),
                      product=StoreStock(id=5, name="Samsung S24", stock_code="SAMSS2412256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"))
                      )
        ])

    def test_order_orderItem_get(self):
        """
        Test to check for order Item and order lists endpoint
        """
        
