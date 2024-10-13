from rest_framework import permissions

class LogsPermissions(permissions.BasePermission):
    """
    Permissions configured to allow only admins and managers access to logs
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['ADMIN', 'MANAGER']