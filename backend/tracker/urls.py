from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CryptocurrencyViewSet, CryptoListViewSet, UserCreateView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cryptocurrencies', CryptocurrencyViewSet)
router.register(r'crypto-lists', CryptoListViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserCreateView.as_view(), name='register'),
    # Token Endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
