import pandas as pd
import requests
import datetime as dt
from dotenv import load_dotenv
import os
import smtplib

load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

# Open Weather API constants
API_KEY = os.getenv("OWM_API_KEY")
LAT = 35.867512
LON = -78.606628
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
RAIN_ID = 700

# Email Related Constants
MY_EMAIL = os.getenv("MyEmail2")
MY_PASSWORD = os.getenv("Email2AppPassword")
TO_EMAIL = os.getenv("MyEmail1")

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
    "units": 'imperial'
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

forecasts_json = response.json()

will_rain = False
for hour_data in forecasts_json['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < RAIN_ID:
        will_rain = True

def send_email():
    email_subject = f"Today's Forecast Has Rain"
    email_message = f"Subject:{email_subject}\n\nBring an Umbrella!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=email_message)
    print("Email Sent!")

if will_rain:
    print("Bring an Umbrella!")
    send_email()










