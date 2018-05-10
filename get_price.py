import requests


def get_price(limit, num_of_requests):  # количество часовых свечей в одном запросе и количество запросов

    # time = response.json().get('Data')[0].get('time')

    for req in range((num_of_requests) + 1):
        if req == 1:
            url = f'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit={limit}'
            response = requests.get(url)
            data = response.json().get('Data')
        else:
            time = data[0].get('time')
            url_new = f'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit={limit}&toTs={time}'
            response = requests.get(url_new)
            data_new = response.json().get('Data')
            data.insert(0, data_new)
    return data

print(get_price(10, 5))

