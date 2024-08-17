import pandas as pd
import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

# Open Weather API constants
API_KEY = os.getenv("OWM_API_KEY")
LAT = 35.867512
LON = -78.606628
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
RAIN_ID = 700

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

if will_rain:
    print("Bring an Umbrella!")







