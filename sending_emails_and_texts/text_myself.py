 #! python3
# text_myself.py - Defines the textmyself() function that texts a message passed to it as a string

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
MY_NUMBER = os.environ['MY_NUMBER']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']

def text_myself(message):
    twilio_cli = Client(ACCOUNT_SID, AUTH_TOKEN)
    twilio_cli.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)