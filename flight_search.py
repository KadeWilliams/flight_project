import requests
import os
import datetime as dt

TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
tequila_key = os.environ['tequila_key']
header = {
    'apikey': tequila_key
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_code(self, city):
        parameters = {
            'term': city
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=header)
        code = response.json()['locations'][0]['code']
        return code
