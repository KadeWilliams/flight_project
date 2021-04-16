from twilio.rest import Client
import os

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
my_phone = os.environ['my_phone']
twilio_phone = os.environ['twilio_phone']


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def notify(self, list):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Only £{list[0]} to fly from {list[1]}-{list[2]} to {list[3]}-{list[4]}!",
            from_=twilio_phone,
            to=my_phone
        )
        print(message.sid)
