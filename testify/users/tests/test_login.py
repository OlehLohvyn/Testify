from rest_framework.test import APITestCase
from rest_framework import status
from ..models import CustomUser
from rest_framework.authtoken.models import Token


class UserLoginTests(APITestCase):
    def test_login_success(self):
        """Testing successful login"""
        user = CustomUser.objects.create_user(username='testuser', password='testpassword123')
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post('/api/users/login/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Checking if the token is returned

    def test_login_invalid_credentials(self):
        """Testing login with incorrect credentials"""
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post('/api/users/login/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Invalid credentials')