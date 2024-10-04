from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WarehouseStock, StoreStock, Product
from django.db.models import Sum

def calculate_storage_quantity(stock_code):
    """
    This function calculates the total quantity of a particular product.
    It first looks through the warehouse_stock table for products of that particular stock_code and then sums their quantity field.
    Afterwards it also goes through the store_stock table for the same product and sums their quantity field.
    It then returns the sum of both.
    """
    total_warehouse_stock_quantity = WarehouseStock.objects.filter(
        stock_code = stock_code
    ).aggregate(Sum('quantity'))['quantity__sum'] or 0

    total_store_stock_quantity = StoreStock.objects.filter(
        stock_code = stock_code
    ).aggregate(Sum('quantity'))['quantity__sum'] or 0

    total_product_quantity = total_store_stock_quantity + total_warehouse_stock_quantity
    return total_product_quantity
@receiver(post_save, sender=WarehouseStock)
@receiver(post_save, sender=StoreStock)
def create_update_product(sender, instance, created, **kwargs):
    """
    This function creates a signal that automatically creates a database entry in the Product table whenever a warehouse_stock or
    store_stock entry is made.
    """
    stock_code = instance.stock_code
    # checks if the product is already available in the product table since product_code is unique
    product, created = Product.objects.get_or_create(product_code=stock_code)

    # if product not found and needs to be created, products fields are populated in this manner
    if created: 
        product.name = instance.name
        product.category = instance.category
        product.reorder_level = instance.reorder_level
        product.product_code = stock_code

    # we set the quantity field to the total quantity regardless of whether created or found to update quantity field
    product.quantity = calculate_storage_quantity(stock_code)
    product.save()

    
