from rest_framework import serializers
from .models import User, Cryptocurrency, CryptoList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'profile_picture', 'birth_date', 'location']


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'name', 'symbol', 'price', 'last_updated']


class CryptoListSerializer(serializers.ModelSerializer):
    cryptos = CryptocurrencySerializer(many=True, read_only=True)

    class Meta:
        model = CryptoList
        fields = ['id', 'name', 'user', 'cryptos']
