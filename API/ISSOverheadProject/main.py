import requests
from datetime import datetime
import smtplib
import time

MY_MAIL = "email@gmail.com"
APP_PASSWORD = "App password"
MY_LAT = 41.008240
MY_LONG = 28.978359

# Your position is within +5 or -5 degrees of the ISS position.


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG -5):
        return True
    else:
        return False


def is_night():
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
    time_now = datetime.now().hour
    if sunrise >= time_now >= sunset:
        return True


# If the ISS is close to my current position
# ,and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_night() and iss_overhead():
        with smtplib.SMTP_SSL("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_MAIL, APP_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject:ISS is OverHead\n\n"
                                                                         "ISS is over your head. LOOK UP!!!")
