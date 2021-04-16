import requests
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'
header = {
    'apikey': 'yaz6SC1CrRgcDlEfWJRe9tU_eqjd2gDv'
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_code(self, city):
        parameters = {
            'term': city
        }
        response = requests.get(TEQUILA_ENDPOINT, params=parameters, headers=header)
        code = response.json()['locations'][0]['code']
        return code

