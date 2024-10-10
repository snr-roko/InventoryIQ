from django.db import models
from django.conf import settings
from products.models import StoreStock, WarehouseStock 
from storages.models import Store, Warehouse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="customers_created")

    def __str__(self):
        return self.name

status = (
    ('PENDING', 'Pending'),
    ('PAID', 'Paid'),
    ('SHIPPED', 'Shipped'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
)

class Order(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders", null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=100, choices=status, default='PENDING')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="orders_created")

    def __str__(self):
        return f"{self.name} on {self.order_date}"

class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orderItems", null=True, blank=True)  
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderItems")
    product = models.ForeignKey(StoreStock, on_delete=models.PROTECT, related_name="ordeItems")
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name="orderItems")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orderItems_created")

    def __str__(self):
        return self.product

transfer = (
    ('PENDING', 'pending'),
    ('RECEIVED', 'received'),
    ('CANCELLED', 'cancelled')
)

class StockTransfer(models.Model):
    source = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="stocksTransferred")
    destination = models.ForeignKey(Store, on_delete=models.PROTECT, related_name="stocksTransferred")
    stock = models.ForeignKey(WarehouseStock, on_delete=models.PROTECT, related_name="stocksTransferred")
    date_transferred = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    reason = models.TextField()
    status = models.CharField(max_length=100, choices=transfer, default='PENDING')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='transfers_created')

    def __str__(self):
        return f"{self.stock} from {self.source} to {self.destination}"