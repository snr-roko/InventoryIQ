from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from .permissions import UserRegistrationPermission
from django.contrib.auth import get_user_model


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (UserRegistrationPermission,)