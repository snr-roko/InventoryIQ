from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "full_name", "phone_number", "age", "role", "created_by"]
    
    fieldsets = UserAdmin.fieldsets + (
        ("Custom fields", {"fields": ("full_name", "phone_number", "age", "role", "created_by")}),
    )    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "full_name", "age", "role", "created_by", "password1", "password2"),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)