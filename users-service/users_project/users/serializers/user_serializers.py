import re

from django.contrib.auth import get_user_model
from rest_framework import serializers


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