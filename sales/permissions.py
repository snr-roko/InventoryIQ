from rest_framework import permissions

class CustomerPermissions(permissions.BasePermission):
    """
    Admins, Managers, Store Managers, Store Staffs and Staffs all have full permissions on CRUD operations of the customer model
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in ['ADMIN', 'MANAGER', 'STORE_MANAGER', 'STORE_STAFF', 'STAFF']
        else:
            return False
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    
class OrderItemPermissions(permissions.BasePermission):
    """
    Admins, Managers, Store Managers and Store Staffs all have full permissions on CRUD operations of the orderItem model
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in ['ADMIN', 'STORE_MANAGER', 'STORE_STAFF', 'MANAGER']
        else:
            return False
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    
class OrderPermissions(permissions.BasePermission):
    """
    Admins, Managers, Store Managers and Store Staffs all have full permissions on CRUD operations of the order model
    A create action can only be done when the data's status is pending
    An update of status to shipped can only be done when object's status is paid 
    An update of status to delivered can also only be done when object's status is shipped
    An update of status to cancelled can also only be done when object's status is paid, shipped or delivered.
    A destroy action can also only be done when an object's status is pending or cancelled.
    """
    
    allowed_roles = {'ADMIN', 'MANAGER', 'STORE_STAFF', 'STORE_MANAGER'}
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in self.allowed_roles:
            if request.method in permissions.SAFE_METHODS:
                return True
            # ensuring that only pending orders are created
            elif view.action == 'create':
                return request.data.get('status') == 'PENDING'
            else:
                return True 
        else:
            return False        
    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            elif view.action == 'update':
                # A pending order can only be updated as pending or to paid
                if obj.status == 'PENDING':
                    return request.data.get('status') in ['PENDING', 'PAID']
                # A paid order can only be updated to shipped or cancelled due to signals
                elif obj.status == 'PAID':
                    return request.data.get('status') in ['SHIPPED', 'CANCELLED']
                # A shipped order can only be updated as shipped or to delivered or cancelled
                elif obj.status == 'SHIPPED':
                    return request.data.get('status') in ['SHIPPED', 'DELIVERED', 'CANCELLED']
                # A delivered order can only be updated as delivered or to delivered or cancelled
                elif obj.status == 'DELIVERED':
                    return request.data.get('status') in ['SHIPPED', 'DELIVERED', 'CANCELLED']
                # if not the above, then we expect a cancelled order that we want to update to a pending state.
                else:
                    return obj.status == 'CANCELLED' and request.data.get('status') == 'PENDING'
            elif view.action == 'partial_update':
                # A pending order can only be updated as pending or to paid
                if obj.status == 'PENDING':
                    return not request.data.get('status') or request.data.get('status') == 'PAID'
                # A paid order can only be updated to shipped or cancelled and can not be updated as paid due to signals
                elif obj.status == 'PAID':
                    return request.data.get('status') and request.data.get('status') in ['SHIPPED', 'CANCELLED']
                # A shipped order can only be updated as shipped or to delivered or cancelled
                elif obj.status == 'SHIPPED':
                    return not request.data.get('status') or request.data.get('status') in ['DELIVERED', 'CANCELLED']
                # A delivered order can only be updated as delivered or to delivered or cancelled
                elif obj.status == 'DELIVERED':
                    return not request.data.get('status') or request.data.get('status') in ['SHIPPED', 'DELIVERED', 'CANCELLED']
                # if not the above, then we expect a cancelled order that we want to update to a pending state.
                else:
                    return obj.status == 'CANCELLED' and request.data.get('status') and request.data.get('status') == 'PENDING'                
            # The only orders that can be deleted are pending orders and cancelled orders.
            elif view.action == 'destroy':
                return obj.status in ['PENDING', 'CANCELLED']
            else:
                return False        
    
class StockTransferPermissions(permissions.BasePermission):
    """
    Read Permissions (Collections and Resources)
        Admins, Managers, Warehouse Managers, Store Managers

    Create Permissions
        A stock Transfer can only be made when incoming data's status is pending
        Only Admins, Managers, Warehouse Managers can create Stock transfers

    Update Permissions
        If status is being updated to received and quantity is not being updated then user must be a store manager, manager or admin
        If status is not being changed and the object's status is pending then user must be a warehouse manager, manager or admin
        Cancelled permissions
            A status can be updated to cancelled when object's status is received.
            User must be a warehouse manager, store manager, manager or admin
            Cancelled will revert stocks back to warehouse
        other update permissions are not allowed
    Delete Permissions
        An object can be deleted when object's status is pending or cancelled.
        If pending, then user must be a warehouse manager, manager or admin
        If cancelled, then user must be a store manager, manager or admin
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER'}
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in self.allowed_roles
            elif view.action == 'create':
                return request.data.get('status') == 'PENDING' and request.user.role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER']
            else:
                return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in self.allowed_roles
            elif view.action == 'partial_update':
                if request.data.get('status') == 'RECEIVED' and obj.status == 'PENDING':
                    return request.user.role in ['ADMIN', 'MANAGER', 'STORE_MANAGER'] and 'quantity' not in request.data
                elif not request.data.get('status') and obj.status == 'PENDING':
                    return request.user.role in ['ADMIN', 'WAREHOUSE_MANAGER', 'MANAGER']
                elif request.data.get('status') == 'CANCELLED' and obj.status == 'RECEIVED':
                    return request.user.role in self.allowed_roles 
                elif request.data.get("status") == 'PENDING' and obj.status == 'CANCELLED':
                    return request.user.role in ['WAREHOUSE_MANAGER', 'ADMIN', 'MANAGER']
                else:
                    # we return false to make sure no other operation is approved due to signals
                    return False
            elif view.action == 'update':
                if request.data.get('status') == 'RECEIVED' and obj.status == 'PENDING':
                    return request.user.role in ['ADMIN', 'MANAGER', 'STORE_MANAGER'] and request.data.get('quantity') == obj.quantity
                elif request.data.get('status') == 'PENDING' and obj.status == 'PENDING':
                    return request.user.role in ['ADMIN', 'WAREHOUSE_MANAGER', 'MANAGER']
                elif request.data.get('status') == 'CANCELLED' and obj.status == 'RECEIVED':
                    return request.user.role in self.allowed_roles
                elif request.data.get('status') == 'PENDING' and obj.status == 'CANCELLED':
                    return request.user.role in ['WAREHOUSE_MANAGER', 'ADMIN', 'MANAGER']
                else:
                    # we return false to make sure no other operations are allowed due to signals
                    return False
            elif view.action == 'destroy':
                if obj.status == 'PENDING':
                    return request.user.role in ['MANAGER', 'ADMIN'] or request.user == obj.created_by
                elif obj.status == 'CANCELLED':
                    return request.user.role in self.allowed_roles
                else:
                    return False
            else:
                return False
     