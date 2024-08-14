import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 35.791538
MY_LONG = -78.781120
MY_EMAIL = ""
MY_PASSWORD = ""
TO_EMAIL = ""

def send_email():
    email_subject = f"ISS is Overhead!"
    email_message = f"Subject:{email_subject}\n\nISS is Overhead, Look up!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=email_message)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Function for: Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead_current_location():
    if (iss_latitude - MY_LAT <= 5) & (iss_longitude - MY_LONG <= 5):
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])-4
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])-4+24
time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark

def during_the_night():
    if (time_now.hour > sunset) & (time_now.hour < sunrise):
        return True
    else:
        return False

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while (during_the_night() == True) and (iss_overhead_current_location() == True):
    time.sleep(60)
    send_email()






