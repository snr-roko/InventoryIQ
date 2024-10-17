from rest_framework.permissions import BasePermission
from rest_framework import permissions

class WarehouseStockPermissions(BasePermission):
    """
    Admins, managers, and warehouse managers have full permissions
    Except stock_code can not be updated
    All other roles do not have access to any actions
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER'}

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_roles
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if view.action == 'update':
            return request.data.get("stock_code") == obj.stock_code
        elif view.action == 'partial_update':
            return not request.data.get("stock_code")
        else:
            return view.action in ["get", "retrieve", "destroy"]

class StoreStockPermissions(BasePermission):
    """
    Admins, manager, Store managers, and store staffs have permissions
    Except stock_code can not be updated
    delete is not allowed for store staff
    All other roles do not have access to any actions
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'STORE_MANAGER', 'STORE_STAFF'}
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_roles
        else: 
            return False
    def has_object_permission(self, request, view, obj):
        if view.action == 'update':
            return request.data.get("stock_code") == obj.stock_code
        elif view.action == 'partial_update':
            return not request.data.get("stock_code")
        elif view.action == 'destroy':
            return request.user.role in {'ADMIN', 'MANAGER', 'STORE_MANAGER'}
        else:
            return request.method in permissions.SAFE_METHODS
        
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
    Admins and Managers can update product image and reorder levels 
    Admins and Managers can delete inactive products
    All other roles do not have access to any action.
    """
    allowed_roles = {'ADMIN', 'MANAGER', 'WAREHOUSE_MANAGER', 'STORE_MANAGER', 'STAFF'}

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in self.allowed_roles:
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'partial_update':
            if len(request.data) == 2:
                return request.data.get("product_image") and request.data.get("reorder_level")
            elif len(request.data) == 1:
                return request.data.get("product_image") or request.data.get("reorder_level")
            else:
                return False
        elif view.action == 'destroy':
            return not obj.active and request.user.role in ['ADMIN', 'MANAGER']
        else:
            return view.action in ['retrieve', 'get']