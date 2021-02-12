import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Environment Variable to store the API key

api_key = os.environ.get('OWN_API_KEY')
account_sid = os.environ['ACC_SID']
auth_token = os.environ['AUTH_TOKEN']

weather_params = {
    "lat": "12.971599",
    "lon": "77.594566",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18287053749",
        to="+919563419038"
    )
    print(message.status)

