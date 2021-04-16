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
prices = dm.get_prices()
users = dm.get_users()

# Updates the dictionary element for the appropriate IATA Code corresponding to the city column

for elem in prices:
    if elem['iataCode'] == '':
        dm.update_iata_code(elem)

for elem in prices:
    fd = FlightData()
    data = fd.get_prices(elem['iataCode'])
    if data[0] < int(elem['lowestPrice']):
        nm = NotificationManager()
        # nm.notify(data)
        for j in users:
            nm.send_emails(data, j['email'])
