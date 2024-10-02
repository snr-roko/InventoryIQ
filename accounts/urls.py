from django.urls import path
from .views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView                                                                                                                                                                                

urlpatterns = [
    path("users/register", UserRegistrationView.as_view(), name='register'),
    path("users/login", TokenObtainPairView.as_view(), name='login'),
    path("users/login/refresh", TokenRefreshView.as_view(), name='login_refresh')
]