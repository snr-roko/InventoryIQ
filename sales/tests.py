from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Order, OrderItem, StockTransfer
from products.models import ProductCategory, StoreStock
from django.urls import reverse

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
            StoreStock(id=1, name="Samsung S21", stock_code="SAMSS2112256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), barcode="2723747937124", price=799.00),
            StoreStock(id=2, name="Samsung S22", stock_code="SAMSS2216256BLUE", quantity=60, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=999.00),
            StoreStock(id=3, name="Samsung S21", stock_code="SAMSS2112256WHITE", quantity=50, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=799.00),
            StoreStock(id=4, name="Samsung S23", stock_code="SAMSS2312256RED", quantity=30, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=1100.00),
            StoreStock(id=5, name="Samsung S24", stock_code="SAMSS2412256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), price=1200.00)
        ])
        Order.objects.bulk_create([
            Order(id=1, status='PENDING'),
            Order(id=2, status='PENDING'),
            Order(id=3, status='PENDING'),
            Order(id=4, status='PENDING'),
        ])

        OrderItem.objects.bulk_create([
            OrderItem(id=1, price=799.00, quantity=3, total_price=2397.00, order=Order(id=1, status='PENDING'),
                      product= StoreStock(id=1, name="Samsung S21", stock_code="SAMSS2112256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"), barcode="2723747937124")
                      ),
            OrderItem(id=2, price=899.00, quantity=6, total_price=5394.00, order=Order(id=1, status='PENDING'),
                      product=StoreStock(id=2, name="Samsung S22", stock_code="SAMSS2216256BLUE", quantity=60, reorder_level=10, category=ProductCategory(id=1, name="Phones"))),
            OrderItem(id=3, price=1000.00, quantity=10, total_price=10000.00, order=Order(id=2, status='PENDING'),
                     product=StoreStock(id=4, name="Samsung S23", stock_code="SAMSS2312256RED", quantity=30, reorder_level=10, category=ProductCategory(id=1, name="Phones"))
),
            OrderItem(id=4, price=1200.00, quantity=5, total_price=6000.00, order=Order(id=2, status='PENDING'),
                      product=StoreStock(id=5, name="Samsung S24", stock_code="SAMSS2412256RED", quantity=20, reorder_level=10, category=ProductCategory(id=1, name="Phones"))
                      )
        ])

    def get_token_for_user(self, user):
        token_results = RefreshToken.for_user(user)
        return str(token_results.access_token)
    
    def test_order_orderItem_get(self):
        """
        Test to check for order Item and order lists endpoint
        """
        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        orderItem_uri = reverse("order-items-list")
        order_uri = reverse("orders-list")
        orderItem_response = self.api.get(orderItem_uri)
        order_response = self.api.get(order_uri)
        self.assertEqual(orderItem_response.status_code, status.HTTP_200_OK)
        self.assertEqual(order_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(orderItem_response.data['results']), 4)
        self.assertEqual(len(order_response.data['results']), 4)
        
    def test_order_orderItem_get_denied(self):
        """
        Tests to check for get requests by unpermitted user
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        orderItem_uri = reverse("order-items-list")
        order_uri = reverse("orders-list")
        orderItem_response = self.api.get(orderItem_uri)
        order_response = self.api.get(order_uri)
        self.assertEqual(orderItem_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(order_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_order_orderItem_retrieve(self):
        """
        Test to check for order Item and order single resource endpoint
        """
        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        orderItem_uri = reverse("order-items-detail", args=[1])
        order_uri = reverse("orders-detail", args=[1])
        orderItem_response = self.api.get(orderItem_uri)
        order_response = self.api.get(order_uri)
        self.assertEqual(orderItem_response.status_code, status.HTTP_200_OK)
        self.assertEqual(order_response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(orderItem_response.data, dict))
        self.assertTrue(isinstance(order_response.data, dict))
        self.assertEqual(orderItem_response.data['price'], "799.00")
        self.assertEqual(order_response.data['status'], 'PENDING')
        
    def test_order_orderItem_retrieve_denied(self):
        """
        Test to check for order Item and order single resource endpoint by unpermitted user
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        orderItem_uri = reverse("order-items-detail", args=[1])
        order_uri = reverse("orders-detail", args=[1])
        orderItem_response = self.api.get(orderItem_uri)
        order_response = self.api.get(order_uri)
        self.assertEqual(orderItem_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(order_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_order_orderItem_creation(self):
        """
        Tests to check for order and orderItem creation endpoints 
        """
        new_order = {
            "id": 5,
            "status": "PENDING",
        }
        
        new_order_Item = {
            "id": 5,
            "price": 999.00,
            "quantity": 10,
            "total_price": 9990.00,
            "order": 2,
            "product": 2
        }

        # Logging In
        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        
        # Creating orders and order items
        orderItem_uri = reverse("order-items-list")
        order_uri = reverse("orders-list")
        orderItem_response = self.api.post(orderItem_uri, new_order_Item)
        order_response = self.api.post(order_uri, new_order)

        # Asserting responses
        self.assertEqual(orderItem_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(order_response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(isinstance(orderItem_response.data, dict))
        self.assertTrue(isinstance(order_response.data, dict))
        self.assertEqual(orderItem_response.data['price'], "999.00")
        self.assertEqual(order_response.data['status'], 'PENDING')

    def test_order_creation_denied(self):
        """
        Tests to check for order creation denial through performing unpermitted actions
        """
        new_order = {
            "id": 5,
            "status": "PAID"
        }

        # Logging In
        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        
        # Creating order
        # Deliberately creating a paid order
        order_uri = reverse("orders-list")
        order_response = self.api.post(order_uri, new_order)

        all_orders = Order.objects.count()
        # Asserting responses
        self.assertEqual(order_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_orders, 4)

    def test_order_orderItem_creation_signals(self):
        """
        Tests to check for order and orderItem creation endpoints and signals
        """
        new_order = {
            "id": 5,
            "status": "PENDING",
        }
        
        new_order_Item = {
            "id": 5,
            "price": 999.00,
            "quantity": 10,
            "total_price": 9990.00,
            "order": 5,
            "product": 2
        }

        new_order_Item_two = {
            "id": 6,
            "price": 1100.00,
            "quantity": 5,
            "total_price": 5500.00,
            "order": 5,
            "product": 4            
        }

        another_order_Item = {
            "id": 7,
            "price": 1200.00,
            "quantity": 7,
            "total_price": 8400.00,
            "order": 5,
            "product": 5            
        }

        # Logging In
        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        
        # Creating orders and order items
        orderItem_uri = reverse("order-items-list")
        order_uri = reverse("orders-list")
        order_response = self.api.post(order_uri, new_order)
        self.api.post(orderItem_uri, new_order_Item)
        self.api.post(orderItem_uri, new_order_Item_two)
        self.api.post(orderItem_uri, another_order_Item)

        all_orders = Order.objects.count()
        all_order_items = OrderItem.objects.count()
        # Asserting orders and order items
        self.assertEqual(order_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(all_orders, 5)
        self.assertEqual(all_order_items, 7)
        
        # Checking if orders total amount equates all order items linked
        # Retrieving particular order
        new_order_uri = reverse("orders-detail", args=[5])
        signal_order_response = self.api.get(new_order_uri)

        # Asserting order
        self.assertEqual(signal_order_response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(signal_order_response.data, dict))
        order_items_total_prices = new_order_Item['total_price'] + new_order_Item_two["total_price"] + another_order_Item["total_price"]
        self.assertEqual(signal_order_response.data['total_amount'], f"{order_items_total_prices:.2f}")

    def test_order_orderItem_update(self):
        """
        Test to check for updates of order Item and order resource endpoint
        """
        update_order = {
            "status": 'PAID'
        }

        update_orderItem = {
            "price": 899.00,
            "quantity": 8,
            "total_price": 7192.00
        }

        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        orderItem_uri = reverse("order-items-detail", args=[1])
        order_uri = reverse("orders-detail", args=[1])
        orderItem_response = self.api.patch(orderItem_uri, update_orderItem)
        order_response = self.api.patch(order_uri, update_order)
        self.assertEqual(orderItem_response.status_code, status.HTTP_200_OK)
        self.assertEqual(order_response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(orderItem_response.data, dict))
        self.assertTrue(isinstance(order_response.data, dict))
        self.assertEqual(orderItem_response.data['price'], "899.00")
        self.assertEqual(order_response.data['status'], 'PAID')
    
    def test_order_update_denied(self):
        """
        Test to check for updates of order Item and order resource denial by performing unpermitted actions 
        """
        update_order = {
            "status": 'SHIPPED'
        }

        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        # updating order
        # Deliberately updating pending to shipped
        order_uri = reverse("orders-detail", args=[1])
        order_response = self.api.patch(order_uri, update_order)

        all_orders = Order.objects.count()
        # Asserting responses
        self.assertEqual(order_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(all_orders, 4)

    def test_order_orderItems_update_signals(self):
        """
        Test to check for updates of order Item and order signals which trigger decrease and increase of storestocks 
        """
        update_order = {
            "status": 'PAID'
        }

        new_update_order = {
            "status": 'CANCELLED'
        }

        token = self.get_token_for_user(self.store_staff_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        # updating order to paid
        order_uri = reverse("orders-detail", args=[1])
        self.api.patch(order_uri, update_order)
        storestock_one = StoreStock.objects.get(id=1)
        storestock_two = StoreStock.objects.get(id=2)
        
        # asserting for quantity changes
        self.assertEqual(storestock_one.quantity, 17)
        self.assertEqual(storestock_two.quantity, 54)

        # updating order to cancelled to revert changes
        self.api.patch(order_uri, new_update_order) 
        new_storestock_one = StoreStock.objects.get(id=1)
        new_storestock_two = StoreStock.objects.get(id=2)

        # asserting for quantity changes
        self.assertEqual(new_storestock_one.quantity, 20)
        self.assertEqual(new_storestock_two.quantity, 60)

    def test_order_orderItems_delete(self):
        """
        Test to check for deletion of order Item and order endpoints
        """
        token = self.get_token_for_user(self.store_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        orderItem_uri = reverse("order-items-detail", args=[1])
        order_uri = reverse("orders-detail", args=[2])
        # deleting one order item
        order_item_response = self.api.delete(orderItem_uri)
        # asserting orderitems deletion
        self.assertEqual(order_item_response.status_code, status.HTTP_204_NO_CONTENT)
        all_order_items = OrderItem.objects.count()
        self.assertEqual(all_order_items, 3)

        # deleting an order
        order_response = self.api.delete(order_uri)
        # asserting order deletion and respective order items deletion
        self.assertEqual(order_response.status_code, status.HTTP_204_NO_CONTENT)
        all_orders = Order.objects.count()
        self.assertEqual(all_orders, 3)
        new_all_order_items = OrderItem.objects.count()
        self.assertEqual(new_all_order_items, 1) 

    def test_order_delete_denial(self):
        """
        Test to check for deletion of order endpoint by an unpermitted user
        """
        token = self.get_token_for_user(self.warehouse_manager_user)
        self.api.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
   
        order_uri = reverse("orders-detail", args=[2])
        # deleting one order item
        order_response = self.api.delete(order_uri)
        self.assertEqual(order_response.status_code, status.HTTP_403_FORBIDDEN)
        all_orders = Order.objects.count()
        self.assertEqual(all_orders, 4)