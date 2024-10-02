from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserRegistrationSerializer, UserListSerializer
from .permissions import UserRegistrationPermission
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (IsAuthenticated, UserRegistrationPermission)

    def get_serializer_context(self):
        return {'request': self.request}
    
class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    # Filtering data returned based on the requst.user's role
    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return get_user_model().objects.all()
        elif user.role == 'STAFF':
            return get_user_model().objects.filter(role__in=['STAFF', 'STORE_STAFF', 'WAREHOUSE_STAFF'])
        elif user.role in ['WAREHOUSE_MANAGER', 'STORE_MANAGER'] :
            return get_user_model().objects.filter(role__in=['STORE_STAFF', 'WAREHOUSE_STAFF', 'STAFF', 'MANAGER', 'STORE_MANAGER', 'WAREHOUSE_MANAGER'])
        elif user.role in ['WAREHOUSE_STAFF', 'STORE_STAFF']:
            return get_user_model().objects.filter(role__in=['WAREHOUSE_STAFF', 'STORE_STAFF'])
        else:
            return get_user_model().objects.none()