import os
import requests
import datetime as dt

tequila_key = os.environ['tequila_key']
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
header = {
    'apikey': tequila_key
}

# dd/mm/yyyy
now = dt.datetime.now()

today = now.today()

one_day = dt.timedelta(days=1)
future_days = dt.timedelta(days=180)

tomorrow = today + one_day
six_months = today + future_days

tomorrow = tomorrow.strftime('%d/%m/%Y')
six_months = six_months.strftime('%d/%m/%Y')


class FlightData:
    # This class is responsible for structuring the flight data.
    def get_prices(self, iataCode):
        parameters = {
            'fly_from': 'LON',
            'fly_to': iataCode,
            'date_from': tomorrow,
            'date_to': six_months,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'curr': 'GBP'
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/search", params=parameters, headers=header)
        data = response.json()['data'][0]
        price = data['price']
        departure_city = data['cityFrom']
        departure_airport = data['cityCodeFrom']
        arrival_city = data['cityTo']
        arrival_airport = data['cityCodeTo']
        items = []
        items.append(int(price))
        items.append(departure_city)
        items.append(departure_airport)
        items.append(arrival_city)
        items.append(arrival_airport)

        return items
