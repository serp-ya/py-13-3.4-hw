from pprint import pprint

import requests

def get_token():
    return 'AQAAAAANuCzYAATopEPaH7-Ma0xMjVIr9SiEw3o'


class YaMetrikaBase:
    api_metrics_url = 'https://api-metrika.yandex.ru/stat/v1/data'
    api_counters_url = 'https://api-metrika.yandex.ru/management/v1/counters'

    def __init__(self, token):
        self.token = token
        self.headers = self.get_headers()

    def get_headers(self):
        return {
            'Authorization': f'OAuth {self.token}'
        }

    def make_request(self, url, params=None):
        return requests.get(url, params=params, headers=self.headers)

    def get_counters(self):
        return self.make_request(self.api_counters_url)

    @staticmethod
    def show_metrics_counter(raw_data):
        pprint(raw_data['data'][0]['metrics'])


class YaMetrikaCounterStats(YaMetrikaBase):

    def __init__(self, token, counter_id):
        self.counter_id = counter_id
        super().__init__(token)

    def get_metrics_data(self, metrics):
        params = {
            'id': self.counter_id,
            **metrics
        }

        return self.make_request(self.api_metrics_url, params).json()

    def get_visits_data(self):
        return self.get_metrics_data({'metrics': 'ym:s:visits'})

    def get_pageviews_data(self):
        return self.get_metrics_data({'metrics': 'ym:s:pageviews'})

    def get_users_data(self):
        return self.get_metrics_data({'metrics': 'ym:s:users'})


if __name__ == '__main__':
    show_metrics_counter = YaMetrikaBase.show_metrics_counter
    counters_list = [counter['id'] for counter in YaMetrikaBase(get_token()).get_counters().json()['counters']]

    for counter_id in counters_list:
        ya_base = YaMetrikaCounterStats(get_token(), counter_id)

        print(f'Счётчик номер: {counter_id}')

        print('Визиты:')
        show_metrics_counter(ya_base.get_visits_data())

        print('Просмотры:')
        show_metrics_counter(ya_base.get_pageviews_data())

        print('Посетители:')
        show_metrics_counter(ya_base.get_users_data())
