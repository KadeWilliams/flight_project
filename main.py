from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import os

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
tequila_key = os.environ['tequila_key']
auth = os.environ['Authorization']
my_phone = os.environ['my_phone']
twilio_phone = os.environ['twilio_phone']

dm = DataManager()
sheet_data = dm.get_data()

# Updates the dictionary element for the appropriate IATA Code corresponding to the city column

for elem in sheet_data:
    if elem['iataCode'] == '':
        dm.update_iata_code(elem)

for elem in sheet_data:
    fd = FlightData()
    data = fd.get_prices(elem['iataCode'])
    if data[0] < int(elem['lowestPrice']):
        nm = NotificationManager()
        nm.notify(data)
