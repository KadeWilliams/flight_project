import requests
from flight_search import FlightSearch

SHEETY_ENDPOINT = 'https://api.sheety.co/a2f0b06de8b5c1d6f115132939c277f7/flightDeals/prices'
header = {
    'Authorization': 'Bearer zf#T3WgPDmM*HbFAUtujz37BJq9a%8RA'
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=header)
        data = response.json()['prices']
        return data

    def update_iata_code(self, dict):
        if dict['iataCode'] == '':
            fs = FlightSearch()
            iata_code = fs.get_code(dict['city'])
            body = {
                'price': {
                    'iataCode': iata_code
                }
            }
            response = requests.put(f'{SHEETY_ENDPOINT}/{dict["id"]}', json=body, headers=header)
            print(response.text)
