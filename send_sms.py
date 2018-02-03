import os
from twilio.rest import Client

twilio_sid = os.environ['TWILIO_SID']
twilio_tkn = os.environ['TWILIO_TKN']
twilio_nbr = os.environ['TWILIO_NBR']

client = Client(twilio_sid, twilio_tkn)

message = client.messages.create(
    to="+12092104311", 
    from_=twilio_nbr,
    body="Greetings! The current time is: 13:37 TKXVLMK32ZTTKR9")

print(message.sid)

