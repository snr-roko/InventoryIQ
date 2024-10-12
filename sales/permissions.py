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
    
    allowed_roles = ['ADMIN', 'MANAGER', 'STORE_STAFF', 'STORE_MANAGER']
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in self.allowed_roles:
            if request.method in permissions.SAFE_METHODS:
                return True
            elif view.action == 'create':
                return request.data['status'] == 'PENDING'
            else:
                return True 
        else:
            return False        
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.role in self.allowed_roles:
            if request.method in permissions.SAFE_METHODS:
                return True
            elif view.action in ['partial_update', 'update']:
                if request.data['status'] == 'SHIPPED':
                    return obj.status == 'PENDING'
                elif request.data['status'] == 'DELIVERED':
                    return obj.status == 'SHIPPED'
                elif request.data['status'] == 'CANCELLED':
                    return obj.status in ['PAID', 'SHIPPED', 'DELIVERED']
                else:
                    return request.data['status'] == 'PAID' and obj.status == 'PENDING'
            elif view.action == 'destroy':
                return obj.status in ['PENDING', 'CANCELLED']
        else:
            return False
    
class StockTransferPermissions(permissions.BasePermission):
    """
    Read Permissions (All and One)
        Admins, Managers, Warehouse Managers, Store Managers

    Create Permissions
        A stock Transfer can only be made when incoming data's status is pending
        Only Admins, Managers, Warehouse Managers can create Stock transfers

    Update Permissions
        If status is not being changed and the object's status is pending then user must be a warehouse manager, manager or admin
        If status is being updated to received and quantity is not being updated then user must be a store manager, manager or admin
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
    allowed_roles = ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER']
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in self.allowed_roles
            elif view.action == 'create':
                return request.data['status'] == 'PENDING' and request.user.role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER']
            else:
                return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in self.allowed_roles
            if view.action in ['update', 'partial_update']:
                if request.data['status'] == 'RECEIVED' and 'quantity' not in request.data:
                    return request.user.role in ['ADMIN', 'MANAGER', 'STORE_MANAGER'] and obj.status == 'PENDING'
                elif not request.data['status'] and obj.status == 'PENDING':
                    return request.user.role in ['ADMIN', 'WAREHOUSE_MANAGER', 'MANAGER']
                elif request.data['status'] == 'CANCELLED':
                    return request.user.role in self.allowed_roles and obj.status == 'RECEIVED'
                else:
                    return False
            elif view.action == 'destroy':
                if obj.status == 'PENDING':
                    return request.user.role in ['MANAGER', 'ADMIN'] or request.user.role == obj.created_by
                elif obj.status == 'CANCELLED':
                    return request.user.role in self.allowed_roles
                else:
                    return False
            else:
                return False            