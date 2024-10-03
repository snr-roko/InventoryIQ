from rest_framework import permissions

class WarehousePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            if view.action == 'list' or request.method in permissions.SAFE_METHODS:
                return user_role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STAFF']
            elif view.action == 'create':
                return user_role in ['ADMIN', 'MANAGER']
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role in ['ADMIN', 'MANAGER']:
                return True
            if user_role in ['WAREHOUSE_MANAGER', 'STAFF']:
                return view.action in ['retrieve', 'update', 'partial_update'] 
        return False

class StorePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            if view.action == 'list' or request.method in permissions.SAFE_METHODS:
                return user_role in ['ADMIN', 'MANAGER', 'STORE_MANAGER', 'STAFF']
            elif view.action == 'create':
                return user_role in ['ADMIN', 'MANAGER']
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role in ['ADMIN', 'MANAGER']:
                return True
            if user_role in ['STORE_MANAGER', 'STAFF']:
                return view.action in ['retrieve', 'update', 'partial_update']
        return False

class SupplierPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            return user_role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STAFF', 'STORE_MANAGER']
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            user_role = request.user.role
            return user_role in ['ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STAFF', 'STORE_MANAGER']
        return False