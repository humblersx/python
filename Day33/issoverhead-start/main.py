import requests
from datetime import datetime
import smtplib



MY_LAT = 39.961178
MY_LONG = -82.998795

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()
hour_now = time_now.hour

# Function if ISS within 5 of my long/lat
def is_near():
    if (abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude <= 5)) and (hour_now >= sunset or hour_now <= sunrise):
        return True
    else:
        return False


#If the ISS is close to my current position
# and it is currently dark
# Email info
my_email = "MYEMAIL@gmail.com"
password = 'PASSWORD'

if is_near():
    # # Send letter
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="EMAIL@gmail.com",
            msg=f"Subject: ISS Spotted Nearby!\n\nLook up!"
        )









