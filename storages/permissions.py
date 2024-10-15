from rest_framework import permissions

class WarehousePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            # for collection get requests; admin, manager, warehouse manager, and staff have permission
            if view.action == 'list' or request.method in permissions.SAFE_METHODS:
                return user_role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STAFF']
            # for post requests, only admin and manager have permission
            elif view.action == 'create':
                return user_role in ['ADMIN', 'MANAGER']
            # An initial verification to stop query to the database 
            # Only admins, managers, warehouse managers and staffs have any access to single resources
            elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']: 
                return user_role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STAFF']
        return False
    
    def has_object_permission(self, request, view, obj):
            user_role = request.user.role
            # for admins and managers, full control to resources are given
            if user_role in ['ADMIN', 'MANAGER']:
                return True
            # for warehouse managers and staffs, they can not delete
            # others are not allowed
            elif user_role in ['WAREHOUSE_MANAGER', 'STAFF']:
                return view.action in ['retrieve', 'update', 'partial_update'] 
            else:
                return False

class StorePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            # for collection get requests; admin, manager, store manager, and staff have permission
            if view.action == 'list' or request.method in permissions.SAFE_METHODS:
                return user_role in ['ADMIN', 'MANAGER', 'STORE_MANAGER', 'STAFF']
            # for post requests, only admin and manager have permission
            elif view.action == 'create':
                return user_role in ['ADMIN', 'MANAGER']
            # An initial verification to stop query to the database 
            # Only admins, managers, store managers and staffs have any access to single resources            
            elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']: 
                return user_role in ['ADMIN', 'MANAGER', 'STORE_MANAGER', 'STAFF'] 
        return False
    
    def has_object_permission(self, request, view, obj):
            user_role = request.user.role
            # for admins and managers, full control to resources are given
            if user_role in ['ADMIN', 'MANAGER']:
                return True
            # for store managers and staffs, they can not delete
            # others are not allowed
            elif user_role in ['STORE_MANAGER', 'STAFF']:
                return view.action in ['retrieve', 'update', 'partial_update']
            else:
                return False

class SupplierPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            # Admins, managers, warehouse managers, staffs, and store managers all have full access
            return user_role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STAFF', 'STORE_MANAGER']
        return False
    
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
