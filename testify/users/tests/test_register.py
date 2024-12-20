from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import CustomUser


class UserLoginTests(APITestCase):

    def test_register_existing_username(self):
        """Testing registration with an existing username"""
        existing_user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword123',
            email='testuser@example.com'
        )

        data = {
            'username': 'testuser',  # Existing username
            'password': 'newpassword123',
            'email': 'newemail@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_register_missing_username(self):
        """Testing registration with missing username"""
        data = {
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_username_length(self):
        """Testing username length validation."""

        # Username is too short (less than 3 characters)
        short_username = 'a'  # 1 character
        data = {
            'username': short_username,
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)  # Ensure the 'username' error is present

        # Username is too long (more than 150 characters)
        long_username = 'a' * 151  # 151 characters
        data = {
            'username': long_username,
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)  # Ensure the 'username' error is present

        # Username is of valid length (between 3 and 150 characters)
        valid_username = 'validuser'  # Valid username with 9 characters
        data = {
            'username': valid_username,
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)  # Ensure the 'token' is returned in the response

    def test_username_invalid_characters(self):
        """Test that username validation raises error for usernames with non-alphanumeric characters."""
        data = {
            'username': 'test_user!',  # Invalid characters (contains '_', '!')
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)


class UserEmailValidationTests(APITestCase):

    def test_register_email_already_exists(self):
        """Testing registration with an email that already exists"""
        # First, create a user with a specific email
        CustomUser.objects.create_user(username='existinguser', password='password123', email='testuser@example.com')

        data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'email': 'testuser@example.com'  # This email already exists
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'This email is already in use.')

    def test_register_invalid_email_format(self):
        """Testing registration with invalid email format"""
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'invalidemail'  # Invalid email format
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'Enter a valid email address.')

    def test_register_missing_email(self):
        """Testing registration with missing email"""
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_email_length(self):
        """Testing email length validation."""

        # Email is too long
        long_email = 'a' * 255 + '@example.com'  # 255 characters for the name part
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': long_email
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

        # Email is of valid length
        valid_email = 'validuser@example.com'
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': valid_email
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)


class UserPasswordValidationTests(APITestCase):

    def test_register_missing_password(self):
        """Testing registration with missing password"""
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_password_length(self):
        """Testing password length validation."""

        # Password is too long
        long_password = 'a' * 257  # 257 characters
        data = {
            'username': 'testuser',
            'password': long_password,
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

        # Password is of valid length
        valid_password = 'validpassword123'
        data = {
            'username': 'testuser',
            'password': valid_password,
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

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
