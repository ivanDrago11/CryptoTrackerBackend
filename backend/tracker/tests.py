from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tracker.models import User, Cryptocurrency, CryptoList


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'password': 'password123',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')


class CryptocurrencyTests(APITestCase):
    def test_create_cryptocurrency(self):
        """
        Ensure we can create a new cryptocurrency.
        """
        url = reverse('cryptocurrency-list')
        data = {
            'name': 'Bitcoin',
            'symbol': 'BTC',
            'price': '40000.1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cryptocurrency.objects.count(), 1)
        self.assertEqual(Cryptocurrency.objects.get().name, 'Bitcoin')


class CryptoListTests(APITestCase):
    def test_create_cryptolist(self):
        """
        Ensure we can create a new crypto list.
        """
        user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='test@example.com'
        )
        crypto = Cryptocurrency.objects.create(
            name='Bitcoin',
            symbol='BTC',
            price='40000.1234567890'
        )
        url = reverse('cryptolist-list')
        data = {
            'name': 'My Crypto List',
            'user': user.id,
            'cryptos': [crypto.id]
        }
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CryptoList.objects.count(), 1)
        self.assertEqual(CryptoList.objects.get().name, 'My Crypto List')
