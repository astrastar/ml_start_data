import requests

class RequestPrice:
    """
    Limit - number of candels in response, num_request - number of request with given limit
    """
    url1 = 'https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit='

    def __init__(self, limit, num_request):
        self.limit = limit - 1
        self.num_request = num_request

    def first_req(self):
        local_url = f'{self.url1}{self.limit}'
        response = requests.get(local_url)
        return response.json().get('Data')

    def other_req(self):
        request_list = []
        time_to = self.first_req()[0].get('time')
        for req in range((self.num_request) - 1):
            local_url = f'{self.url1}{self.limit + 1}&toTs={time_to}'
            response = requests.get(local_url)
            response_json = response.json().get('Data')
            request_list.extend(response_json[0:-1])
            time_to = response_json[0].get('time')
        return request_list

    @property
    def final_response(self):
        final_res = []
        final_res.extend(self.first_req())
        final_res.extend(self.other_req())
        return final_res


x = RequestPrice(2, 2)
print(len(x.final_response))
print(x.first_req())









