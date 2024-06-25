from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CryptocurrencyViewSet, CryptoListViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cryptocurrencies', CryptocurrencyViewSet)
router.register(r'crypto-lists', CryptoListViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
