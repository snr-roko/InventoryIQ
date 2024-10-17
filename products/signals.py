from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import WarehouseStock, StoreStock, Product
from django.db.models import Sum

def check_low_stocks(model):
    if model.quantity <= model.reorder_level:
        model.low_stock = True
    else:
        model.low_stock = False

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

    total_product_quantity = total_warehouse_stock_quantity + total_store_stock_quantity
    return total_product_quantity

@receiver(post_save, sender=WarehouseStock)
@receiver(post_save, sender=StoreStock)
def create_update_product(sender, instance, created, **kwargs):
    """
    This function creates a signal that automatically creates a database entry in the Product table whenever a warehouse_stock or
    store_stock entry is made.
    """
    stock_code = instance.stock_code
    # The code below disconnects the signal and saves the instance again after checking for low stocks
    post_save.disconnect(create_update_product, sender=WarehouseStock)
    post_save.disconnect(create_update_product, sender=StoreStock)
    check_low_stocks(instance)
    instance.save()
    post_save.connect(create_update_product, sender=WarehouseStock)
    post_save.connect(create_update_product, sender=StoreStock)

    # checks if the product is already available in the product table since product_code is unique
    try:
        product= Product.objects.get(product_code=stock_code)
        product.name = instance.name
        product.category = instance.category
        product.quantity = calculate_storage_quantity(stock_code)
        product.active = True
        product.save()
    except Product.DoesNotExist:
        # When the product has to be created
        Product.objects.create(
            name = instance.name,
            product_code = stock_code,
            category = instance.category,
            quantity = calculate_storage_quantity(stock_code),
            active = True,
            reorder_level = instance.reorder_level or 0
        )    

@receiver(post_save, sender=Product)
def set_low_stocks(sender, instance, created, **kwargs):
    """
    This signal function is used to automatically set low stocks of the models to True when stocks are lower 
    than reorder levels
    """
    post_save.disconnect(set_low_stocks, sender=Product)
    check_low_stocks(instance)
    instance.save()
    post_save.connect(set_low_stocks, sender=Product)

@receiver(post_delete, sender=WarehouseStock)
@receiver(post_delete, sender=StoreStock)
def update_delete_product(sender, instance, **kwargs):
    """
    This is a signal to automatically recalculate product quantity whenever a warehouse stock or store stock is deleted
    When the product quantity recalculated is zero, the product is also deactivated
    """
    stock_code = instance.stock_code

    # we try finding the product
    try:
        product = Product.objects.get(product_code=stock_code)
        # we calculate the total quantity across storages
        total_quantity = calculate_storage_quantity(stock_code)
        # if total quantity is zero, we deactivate the product
        if total_quantity == 0:
            product.quantity = total_quantity
            product.deactivate()
        # if the total quantity is still more than zero, meaning other storages have stock
        # we set the product quantity to that storage quantity
        else:
            product.quantity = total_quantity
            product.active = True
            product.last_active_date = None
            product.save()
    # the product was not found, nothing has to be done then
    except Product.DoesNotExist:
        pass

    
