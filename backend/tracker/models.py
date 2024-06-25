# backend/tracker/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

    # Specify unique related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Unique related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    market_cap = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    volume_24h = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class CryptoList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptos = models.ManyToManyField(Cryptocurrency, blank=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"
