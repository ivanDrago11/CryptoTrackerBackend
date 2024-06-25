# backend/tracker/management/commands/fetch_crypto_data.py
import requests
from django.core.management.base import BaseCommand
from tracker.models import Cryptocurrency


class Command(BaseCommand):
    help = 'Fetch cryptocurrency data from CoinGecko API and update the database'

    def handle(self, *args, **kwargs):
        url = 'https://api.coingecko.com/api/v3/coins/markets'
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': 'false'
        }
        response = requests.get(url, params=params)
        data = response.json()

        for crypto in data:
            name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['current_price']
            market_cap = crypto['market_cap']
            volume_24h = crypto['total_volume']

            obj, created = Cryptocurrency.objects.update_or_create(
                symbol=symbol,
                defaults={
                    'name': name,
                    'price': price,
                    'market_cap': market_cap,
                    'volume_24h': volume_24h,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Created cryptocurrency {name} ({symbol})'))
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'Updated cryptocurrency {name} ({symbol})'))
