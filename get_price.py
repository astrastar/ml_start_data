import requests


def get_price(limit):
    time = 000000
    url = f'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit={limit}&toTs={time}'
    response = requests.get(url)
    return response.json().get('Data')

