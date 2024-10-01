from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager



class CustomBaseManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Username Required")
        if not email: 
            raise ValueError("Email Required")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'ADMIN')

        return self.create_user(username, email, password, **extra_fields)
        

# Custom user model
class CustomUser(AbstractUser):
    # Roles that a user created will have
    ROLES = (
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('STAFF', 'Staff'),
        ('WAREHOUSE_MANAGER', 'Warehouse Manager'),
        ('WAREHOUSE_STAFF', 'Warehouse Staff'),
        ('STORE_MANAGER', 'Store Manager'),
        ('STORE_STAFF', 'Store Staff')
    )

    # A link to the user model's manager
    objects = CustomBaseManager()
    full_name = models.CharField(max_length=255)
    phone_number =  models.CharField(max_length=10, unique=True)
    age = models.PositiveIntegerField(null=True)
    role = models.CharField(max_length=30, choices=ROLES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='created_users', null=True)

    def __str__(self):
        return self.full_name


class UserProfile(models.Model):
    date_of_birth = models.DateField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', max_length=255, null=True, blank=True)

    def __str__(self):
        return "{} Profile".format(self.user.first_name)

