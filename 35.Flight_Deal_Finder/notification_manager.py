from twilio.rest import Client

TWILIO_SID = "ACd88f803136f7778de3980efb321a6626"
TWILIO_AUTH_TOKEN = "c6b371de14efc75a8c7e0c014d051ec6"
TWILIO_VIRTUAL_NUMBER = +18287053749
TWILIO_VERIFIED_NUMBER = +919563419038


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
