import requests

from app.enums import Coin, Currency

API_URL = 'https://api.coingecko.com/api/v3/'
PRICES_RESOURCE = 'coins/{}/contract/%20/market_chart/range?vs_currency={}&from={}&to={}'


def fetch_prices(coin: Coin, currency: Currency, date_from, date_to):
    return requests.get(
        API_URL + PRICES_RESOURCE.format(coin.value, currency.value, date_from, date_to)
    ).json()
