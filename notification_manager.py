from twilio.rest import Client
import os
import smtplib

my_email = 'a.python.smtp.test@gmail.com'

google_flights = 'https://www.google.com/travel/flights'

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
my_phone = os.environ['my_phone']
twilio_phone = os.environ['twilio_phone']


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def notify(self, flight_data: list) -> None:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Only £{flight_data[0]} to fly from {flight_data[1]}-{flight_data[2]} to {flight_data[3]}-{flight_data[4]}!",
            from_=twilio_phone,
            to=my_phone
        )
        print(message.sid)

    def send_emails(self, flight_data: list, their_email: str) -> None:
        message = f"Subject: New Low Price Flight\n\nLow price alert! Only £{flight_data[0]} to fly from {flight_data[1]}-{flight_data[2]} to {flight_data[3]}-{flight_data[4]}!\n{google_flights}?hl=en#flt={flight_data[2]}.{flight_data[4]}.*{flight_data[4]}.{flight_data[2]}"
        message = message.encode('utf-8')
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user='a.python.smtp.test@gmail.com', password='QJcppZ4y69npg7D')
            connection.sendmail(
                from_addr=my_email,
                to_addrs=their_email,
                msg=message
            )
