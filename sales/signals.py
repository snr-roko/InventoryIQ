from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order, OrderItem, StockTransfer
from products.models import StoreStock

@receiver(post_save, sender=OrderItem)
@receiver(post_delete, sender=OrderItem)
def create_update_delete_orderItems(sender, instance, **kwargs):
    """
    This signal function is used to automatically update the total amount and some other fields of the Order model 
    whenever the OrderItem model is created or updated.
    """
    # we set order to the orderItem instance's order field
    order = instance.order
    if order:
        # we look for all order items with that particular order linked to it
        all_order_items = order.orderItems.all()
        total_amount = 0
        # we loop through each order item found
        for orderItem in all_order_items:
            # we set a variable total_amount and add each total_price to it
            total_amount = total_amount + orderItem.total_price
        # we set the total_amount calculated after the loop completes to the total_amount field of that particular order
        order.total_amount = total_amount
        # we then save the order 
        order.save()


@receiver(post_save, sender=Order)
def update_order_paid_cancelled(sender, instance, created, **kwargs):
    """
    This signal function is used to check for when an updated order instance's status is paid.
    If paid, StoreStock's quantity is decreased by the orderItem's quantity.
    If cancelled, Store stock is reversed.
    """
    # We set status to the order instance's status field
    status = instance.status
    if status == 'PAID':
        # if status is paid, then get all orderItems linked with the order instance being updated or created
        all_order_items = instance.orderItems.all()
        # loop through all the order items
        for orderItem in all_order_items:
            # we set the store_stock to each orderItem's product field
            storeStock = orderItem.product
            # we decrease each storestock's quantity by each orderItem's quantity
            storeStock.quantity = storeStock.quantity - orderItem.quantity
            storeStock.save()
    elif status == 'CANCELLED':
        # if status is cancelled, we get all orderitems linked with the order instance
        all_order_items = instance.orderItems.all()
        # we loop through each order item
        for orderItem in all_order_items:
            # we set the storestock to each orderitem's product field
            storeStock = orderItem.product
            # We increase the storestock's quantity by the orderitem's quantity
            storeStock.quantity = storeStock.quantity + orderItem.quantity
            storeStock.save()

@receiver(post_save, sender=StockTransfer)
def update_stock_transfer(sender, instance, created, **kwargs):
    """
    This is a signal function that seeks to increase and decrease warehouse stocks and store stocks
    when a stock transfer is updated.
    """
    status = instance.status
    if status == 'RECEIVED':
        # when the status is received, we get the warehousestock from the instance's stock field
        warehouseStock = instance.stock
        # we decrease the warehouse stock's quantity by the instance's quantity
        warehouseStock.quantity = warehouseStock.quantity - instance.quantity
        stock_code = warehouseStock.stock_code
        store = instance.destination
        # we use the warehouse stock code together with the store - the destination to retrieve the exact store stock code
        try:
            storestock = StoreStock.objects.get(stock_code=stock_code, store=store)
        except StoreStock.DoesNotExist:
            return
        # we increase the quantity of that particular stock code and store combination
        storestock.quantity = storestock.quantity + instance.quantity
        warehouseStock.save()
        storestock.save()
    elif status == 'CANCELLED':
        # when the status is received, we get the warehousestock from the instance's stock field
        warehouseStock = instance.stock
        # we increase the warehouse stock's quantity by the instance's quantity
        warehouseStock.quantity = warehouseStock.quantity + instance.quantity
        stock_code = warehouseStock['stock_code']
        store = instance.destination
        # we use the warehouse stock code together with the store - the destination to retrieve the exact store stock code
        try:
            storestock = StoreStock.objects.get(stock_code=stock_code, store=store)
        except StoreStock.DoesNotExist:
            return
        # we decrease the quantity of that particular stock code and store combination
        storestock.quantity = storestock.quantity - instance.quantity
        warehouseStock.save()
        storestock.save()        