import requests
from datetime import datetime
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# print(response.json()["iss_position"]["longitude"])
# print(response.json()["iss_position"]["latitude"])

MY_LAT = 39.961178
MY_LNG = -82.998795

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}", params=parameters)
response.raise_for_status()
print(response.json())
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

