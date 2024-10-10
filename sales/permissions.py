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
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in ['ADMIN', 'STORE_MANAGER', 'STORE_STAFF', 'MANAGER']
        else:
            return False        
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    
class StockTransferPermissions(permissions.BasePermission):
    """
    Read Permissions (All and One)
        Admins, Managers, Warehouse Managers, Store Managers

    Create Permissions
        A stock Transfer can only be made when status is pending
        Only Admins, Managers, Warehouse Managers can create Stock transfers

    Update Permissions
        Admins and Managers have full permission
        Warehouse Managers can only make updates when Status is pending
        Store Managers can only make updates when update is received but can not update quantity though

        Cancelled permissions
            Only Managers and Admins can update status to cancelled
            Cancelled will revert stocks back to warehouse

    Delete Permissions
        Only when status is pending
        Only Warehouse Managers, Managers and Admins have access
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER']
            elif view.action == 'create':
                return request.data['status'] == 'PENDING' and request.user.role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER']
            else:
                return request.user.role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER']
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER']
            if view.action in ['update', 'partial_update']:
                if request.user.role in ['ADMIN', 'MANAGER']:
                    return True
                elif request.user.role == 'WAREHOUSE_MANAGER':
                    return 'status' not in request.data and obj.status == 'PENDING'
                elif request.user.role == 'STORE_MANAGER':
                    return request.data['status'] == 'RECEIVED' and 'quantity' not in request.data
                else:
                    return False
            elif view.action == 'destroy':
                return request.user.role in ['MANAGER', 'WAREHOUSE_MANAGER', 'ADMIN'] and obj.status == 'PENDING'
            else:
                return False            