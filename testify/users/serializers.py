import re

from django.contrib.auth import get_user_model
from rest_framework import serializers

from testify.users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer for retrieving user details."""

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'help_text': 'The user\'s email address'},
            'first_name': {'help_text': 'The user\'s first name'},
            'last_name': {'help_text': 'The user\'s last name'},
        }

    def validate_email(self, value):
        """Ensure email format is valid."""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Enter a valid email address.")
        return value


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'username': {'help_text': 'The unique username for the user'},
            'password': {'write_only': True, 'help_text': 'The password for the user'},
            'email': {'help_text': 'The user\'s email address', 'required': True},
        }

    def validate_username(self, value):
        # Check if the username is at least 3 characters long
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")

        if len(value) > 150:
            raise serializers.ValidationError("Username must be less than or equal to 150 characters long.")

        # Check if the username contains only letters and numbers
        if not value.isalnum():
            raise serializers.ValidationError("Username can only contain letters and numbers.")

        # Check if the username already exists in the database
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")

        return value

    def validate_email(self, value):
        """Ensure the email is unique and in a valid format."""
        if not value:
            raise serializers.ValidationError("Email is required.")

        if len(value) > 254:
            raise serializers.ValidationError("Email address must be less than or equal to 254 characters long.")

        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def validate_password(self, value):
        """Password length check."""
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if len(value) > 256:
            raise serializers.ValidationError("Password must be less than or equal to 256 characters long.")
        return value

    def create(self, validated_data):
        """Creates a new user instance with the provided validated data."""
        user = get_user_model().objects.create_user(**validated_data)
        return user

