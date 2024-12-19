from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class UserRegistrationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/users/register/'

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(get_user_model().objects.count(), 1)


from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class UserLoginTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = '/api/users/register/'
        self.login_url = '/api/users/login/'
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }

        # Реєструємо користувача
        self.client.post(self.register_url, self.user_data, format='json')

    def test_user_login(self):
        # Логін користувача
        login_data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(self.login_url, login_data, format='json')

        # Перевірка статусу та наявності токену
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        # Перевірка, чи існує токен в базі даних
        token = Token.objects.get(user__username='testuser')
        self.assertEqual(response.data['token'], token.key)
