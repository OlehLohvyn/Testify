from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..models import CustomUser  # Import your custom user model
from django.urls import reverse


class LogoutViewTests(APITestCase):

    def setUp(self):
        # Create a user with a custom model
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        # Create a token for the user
        self.token = Token.objects.create(user=self.user)
        # Header for authentication
        self.auth_header = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}
        # URL for logout
        self.logout_url = reverse('logout')  # Make sure the URL has the correct name

    def test_logout_success(self):
        """Test successful logout"""
        response = self.client.post(self.logout_url, **self.auth_header)
        # Check the response status and message
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], 'Successfully logged out.')
        # Check if the token has been deleted
        self.assertFalse(Token.objects.filter(user=self.user).exists())  # Ensure the token no longer exists

    def test_logout_no_token(self):
        """Test when no token is provided"""
        response = self.client.post(self.logout_url)
        # Check if the response returns a 401 Unauthorized status when no token is provided
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_logout_without_authentication(self):
        """Test when the user is not authenticated"""
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)  # Check if the response contains error details
