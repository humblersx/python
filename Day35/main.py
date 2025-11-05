import requests
from twilio.rest import Client
import os

api_key = "<API_KEY>"
MY_LAT = 39.961178
MY_LONG = -82.998795


#account_sid = "<ACCOUNT_SID>"
#auth_token = "<AUTH_TOKEN>"



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
each = 0
while each < 4:
    #print(weather_data["list"][each]["weather"][0]["id"])
    if int(weather_data["list"][each]["weather"][0]["id"]) < 600:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Bring an umbrella today.",
            from_="whatsapp:+14155238886",
            to="whatsapp:+16145585761",
        )
        print(message.status)
        break
    each += 1




