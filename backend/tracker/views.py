from rest_framework import viewsets, generics
from .models import User, Cryptocurrency, CryptoList
from .serializers import UserSerializer, CryptocurrencySerializer, CryptoListSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework import serializers


# Users CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# Only Registration
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [IsAuthenticated]


class CryptoListViewSet(viewsets.ModelViewSet):
    queryset = CryptoList.objects.all()
    serializer_class = CryptoListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    # Custom JWT Token View for login with username or email


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get('password')
        }

        user_obj = User.objects.filter(email=attrs.get('username')).first(
        ) or User.objects.filter(username=attrs.get('username')).first()
        if user_obj:
            credentials['username'] = user_obj.username
            # credentials['password'] = user_obj.password
        else:
            raise serializers.ValidationError(
                "Invalid username/email or password")

        # # Step 3: Authenticate the user
        user = authenticate(
            username=credentials['username'], password=credentials['password'])
        print(f'authenticaded {user}')
        print('user ' + credentials['username'])
        print('password ' + credentials['password'])
        # print(user)
        # # Step 4: Validate authentication
        # if user:
        #     print("Authentication successful")
        # else:
        #     print("Authentication failed")
        #     raise serializers.ValidationError("Invalid credentials")

        # Pass the validated data to the parent class
        return super().validate(credentials)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
