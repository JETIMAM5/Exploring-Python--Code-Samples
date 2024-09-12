import requests
import os
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACe4ef388556e0580f5d3fc0641f1c2944"
auth_token = os.environ.get("AUTH_TOKEN")

PARAMETERS = {
    "lat": 41.945860,
    "lon": 34.587880,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.Remember to bring an umbrella!",
        from_='+16572206136',
        to='+905536912058')
    print(message.status)


