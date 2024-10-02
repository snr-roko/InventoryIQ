from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    # New fields created to handle password inputs
    class Meta: 
        model = CustomUser
        fields = ("id", "first_name", "last_name", "full_name", "phone_number", "username", "email", "age", "role", "password", "confirm_password")

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    # The above checks whether the two passwords entered are the same.
    def create(self, validated_data):
        validated_data.pop('password')
        validated_data['password'] = validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(read_only = True)

    class Meta:
        model = UserProfile
        fields = ("id", "user", "date_of_birth", "bio", "profile-picture")
