import requests
from datetime import datetime
import smtplib
import time

# Get you coordinates at https://www.latlong.net/

MY_LAT = #your latitude coordinate
MY_LONG = #your longitude coordinate
MY_EMAIL = #YOUR EMAIL
MY_PASSWORD = #YOUR PASSWORD

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude)
    print(iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

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

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
     time.sleep(60)
     if is_iss_overhead() and is_night():
         connection = smtplib.SMTP("smtp.gmail.com", port=587) #Changhe host according to your email provider
         connection.starttls()
         connection.login(user=MY_EMAIL, password=MY_PASSWORD)
         connection.sendmail(from_addr=MY_EMAIL,
                             msg="Subject:Look up in the sky ☝️\n\nISS satellite is passing above your head right now!",
                             to_addrs=MY_EMAIL,
                             )
