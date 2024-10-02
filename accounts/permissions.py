from rest_framework.permissions import BasePermission

class UserRegistrationPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:    
            user_role = request.user.role
            new_user_role = request.data.get('role')
            
            # Users with Admin or manager roles have full access to the registration page
            if user_role in ['ADMIN', 'MANAGER']:
                return True
            # Users with role staff can only create store and warehouse staffs
            elif user_role == 'STAFF':
                return new_user_role in ['WAREHOUSE_STAFF', 'STORE_STAFF']
            # Users with role warehouse manager can only create warehouse staffs
            elif user_role == 'WAREHOUSE_MANAGER':
                return new_user_role == 'WAREHOUSE_STAFF'
            # Users with role store manager can only create store staff
            elif user_role == 'STORE_MANAGER':
                return new_user_role == 'STORE_STAFF'
            else:
                return False
            
    
        