from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from .permissions import UserRegistrationPermission
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (IsAuthenticated, UserRegistrationPermission)