from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+19382533388',
  body='202404031451q',
  to='+8617686026701'
)

print(message)