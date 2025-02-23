from django.urls import path
from .views import UserRegistrationView, UserListView, UserProfileView, UserProfileUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView                                                                                                                                                                                

urlpatterns = [
    path("users/register/", UserRegistrationView.as_view(), name='register'),
    path("users/login/", TokenObtainPairView.as_view(), name='login'),
    path("users/login/refresh/", TokenRefreshView.as_view(), name='login_refresh'),
    path("users/", UserListView.as_view(), name='users'),
    path("profile/me/", UserProfileView.as_view(), name='profile'),
    path("profile-update/me/", UserProfileUpdateView.as_view(), name='profile-update')
]