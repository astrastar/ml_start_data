import requests

class RequestPrice:
    """
    Limit - number of candels in response, num_request - number of request with given limit
    """
    url1 = 'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit='
    final_response = []

    def __init__(self, limit, num_request):
        self.limit = limit
        self.num_request = num_request

    def first_req(self):
        local_url = f'{self.url1}{self.limit}'
        response = requests.get(local_url)
        return response.json().get('Data')

    def other_req(self):
        request_list = []
        time_to = self.first_req()[0].get('time')
        for req in range(self.num_request):
            local_url = f'{self.url1}{self.limit}&toTs={time_to}'
            response = requests.get(local_url)

#
# x = RequestPrice(10, 1)
# print(x.final_response)