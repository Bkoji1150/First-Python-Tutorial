from twilio.rest import Client
from config import account_sid, auth_token, number, twilio_phone, message
from pprint import pprint

client = Client(account_sid, auth_token) 
""" This is to send text message"""

message = client.messages.create(
    to = number,
    from_ = twilio_phone,
    body = message
)
print(message.body)
""" This is for vidoe calls"""
# pprint(dir(client.video))