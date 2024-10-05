from rest_framework.permissions import BasePermission
from rest_framework import permissions

class WarehouseStockPermissions(BasePermission):
    """
    Admins, manager, and warehouse managers have full permissions
    All other roles do not have access to any actions
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER'}

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_roles
        else:
            return False
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class StoreStockPermissions(BasePermission):
    """
    Admins, manager, and Store managers have full permissions
    All other roles do not have access to any actions
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'STORE_MANAGER'}
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_roles
        else: 
            return False
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
        
class ProductCategoryPermissions(BasePermission):
    """
    Admins, Staffs, Managers, Warehouse Managers, and Store Managers have full access
    Other roles do not have access to any actions
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER', 'STAFF'}
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_roles
        else:
            return False
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
        
class ProductPermissions(BasePermission):
    """
    Admins, Managers, Warehouse Managers, Store Managers, and Staff have access to get requests (list and retrieve).
    All other roles do not have access to any action.
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER', 'STAFF'}

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in self.allowed_roles:
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)