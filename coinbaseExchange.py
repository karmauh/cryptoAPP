import requests
import http.client
import json
from datetime  import datetime
from tabulate import tabulate


class CoinbaseExchange(object):
    def __init__(self):
        self.data_json = None
        self._get_data()
        
        
    def _get_data(self):
        conn = http.client.HTTPSConnection("api.exchange.coinbase.com")
        payload = ''
        headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'something',
        }

        conn.request("GET", "/products?status=active", payload, headers)
        res = conn.getresponse()
        data = res.read()
        self.data_json = json.loads(data)
        
        
    def all_pairs(self):
        pairs = sorted([product['id'] for product in self.data_json])
        column_count = 10
        table_data = []
        for i, pair in enumerate(pairs):
            if i % column_count == 0:
                table_data.append([])
            table_data[-1].append(pair)

        print(tabulate(table_data, headers=['Pairs']))
        
        
    def get_price(self, currency_pair, date_time=None):
        if not self.data_json:
            self._get_data()

        if date_time:
            datetime_str = date_time.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            now = datetime.now()
            datetime_str = now.strftime("%Y-%m-%dT%H:%M:%S")

        try:
            if date_time == None:
                url = f'https://api.coinbase.com/v2/prices/{currency_pair}/spot'
            else:
                url = f'https://api.coinbase.com/v2/prices/{currency_pair}/spot?date={datetime_str}'
            response = requests.get(url)
            price = response.json()['data']['amount']

            if date_time:
                print(f'\nPrice {str(currency_pair).upper()} at {date_time.strftime("%H:%M")} on {date_time.strftime("%Y-%m-%d")}: {price}')
            else:
                print(f'\nPrice {str(currency_pair).upper()} at the current time and date: {price}')

            return float(price)
        except:
            print('\nAn error occurred while fetching the price')
            return None
        
        
    def compare_prices(self, currency_pair, purchase_price):
        current_price = self.get_price(currency_pair)

        difference = current_price - purchase_price
        percentage_difference = (difference / purchase_price) * 100

        print(f'Purchase price for {str(currency_pair).upper()}: {purchase_price}')
        print(f'Current price for {str(currency_pair).upper()}: {current_price}')
        print(f'Difference: {difference:.2f} ({percentage_difference:.2f}%)')