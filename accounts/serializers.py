from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CustomUser
        fields = ("id", "first_name", "last_name", "full_name", "phone-number", "username", "email", "age", "role")
        extra_kwargs = {'password': {'write-only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = UserProfile
        fields = ("id", "user", "date_of_birth", "bio", "profile-picture")
