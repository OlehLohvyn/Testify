from rest_framework.test import APITestCase
from rest_framework import status
from ..models import CustomUser
from rest_framework.authtoken.models import Token


class UserRegisterTests(APITestCase):

    def test_register_success(self):
        """Testing successful user registration"""
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)  # Checking if the token is returned

        # Checking if the user is created in the database
        user = CustomUser.objects.get(username='testuser')
        self.assertTrue(user.check_password('testpassword123'))

    def test_register_invalid_data(self):
        """Testing registration with incomplete data"""
        data = {
            'username': 'testuser'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)  # Checking if there is an error for missing password