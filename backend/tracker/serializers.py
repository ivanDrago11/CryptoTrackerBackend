from rest_framework import serializers
from .models import User, Cryptocurrency, CryptoList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        # user.set_password(validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id', 'name', 'symbol',
                  'price', 'market_cap', 'volume_24h', 'last_updated']


class CryptoListSerializer(serializers.ModelSerializer):
    # cryptos = CryptocurrencySerializer(many=True, read_only=True)
    cryptos = serializers.PrimaryKeyRelatedField(
        queryset=Cryptocurrency.objects.all(), many=True)

    class Meta:
        model = CryptoList
        fields = ['id', 'name', 'user', 'cryptos']
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        cryptos_data = validated_data.pop('cryptos')
        cryptoList = CryptoList.objects.create(**validated_data)
        cryptoList.cryptos.set(cryptos_data)
        return cryptoList
