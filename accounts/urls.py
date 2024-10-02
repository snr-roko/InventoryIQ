from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path("users/register", UserRegistrationView.as_view(), name='register')
]