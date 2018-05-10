import requests


def get_price(limit):
    url = f'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit={limit}'
    response = requests.get(url)
    return response.json().get('Data')

