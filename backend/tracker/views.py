from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User, Cryptocurrency, CryptoList
from .serializers import UserSerializer, CryptocurrencySerializer, CryptoListSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this view


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [AllowAny]  # Allow anyone to access this view


class CryptoListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CryptoList.objects.all()
    serializer_class = CryptoListSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this view
