from twilio.rest import Client
import os
account_sid = os.environ['acc_ssid']
auth_token = os.environ['auth_token']
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='Number',
  to='Number',
  body='Hi Mom'
)

print(message.sid)
