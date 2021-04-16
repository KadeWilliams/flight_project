import os

import requests
from flight_search import FlightSearch

auth = os.environ['Authorization']

SHEETY_ENDPOINT_PRICES = 'https://api.sheety.co/a2f0b06de8b5c1d6f115132939c277f7/flightDeals/prices'
SHEETY_ENDPOINT_USERS = 'https://api.sheety.co/a2f0b06de8b5c1d6f115132939c277f7/flightDeals/users'
header = {
    'Authorization': auth
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_prices(self):
        response = requests.get(SHEETY_ENDPOINT_PRICES, headers=header)
        data = response.json()['prices']
        return data

    def get_users(self):
        response = requests.get(SHEETY_ENDPOINT_USERS, headers=header)
        data = response.json()['users']
        return data

    def update_iata_code(self, dict):
        fs = FlightSearch()
        iata_code = fs.get_code(dict['city'])
        body = {
            'price': {
                'iataCode': iata_code
            }
        }
        response = requests.put(f'{SHEETY_ENDPOINT_PRICES}/{dict["id"]}', json=body, headers=header)
        print(response.text)
