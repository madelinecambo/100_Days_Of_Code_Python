import pandas as pd
import requests
import datetime as dt
from dotenv import load_dotenv
import os
from weather import check_rain, check_cold_rule, check_heat_rule, format_weather_email, send_email
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

# Open Weather API constants
API_KEY = os.getenv("OWM_API_KEY")
LAT = os.getenv("MY_LAT")
LON = os.getenv("MY_LON")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LOW_TEMP_FEELS_LIKE = 35
HIGH_TEMP_FEELS_LIKE = 100
RAIN_ID = 700

# Date Constants
TODAY = dt.datetime.now().date()
MATCH_START_TIME = pd.to_datetime(str(TODAY) + ' ' + "18:00:00").strftime('%H:%M:%S')
TOURNAMENT_DATES = ['2024-08-29','2024-08-31', '2024-09-01', '2024-09-02']
COMBO_MATCH_DATES = ['2024-08-17', '2024-08-19', '2024-08-20', '2024-08-26', '2024-09-02', '2024-09-09', '2024-09-16', '2024-09-23']
MIXED_MATCH_DATES = ['2024-09-13', '2024-09-21', '2024-09-28', '2024-10-05', '2024-10-26', '2024-11-01', '2024-11-09', '2024-11-23']

ALL_DATES = TOURNAMENT_DATES + COMBO_MATCH_DATES + MIXED_MATCH_DATES
ALL_DATES = [pd.to_datetime(date).date() for date in ALL_DATES]

if TODAY in ALL_DATES:
    print("There is a match today!")

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

    weather_ids = []
    forecast_3hr = forecasts_json['list']

    for idx, forecast in enumerate(forecast_3hr):
        weather_ids.append(forecast['weather'][0]['id'])
        print(forecast)
        if pd.to_datetime(forecast['dt_txt']).strftime('%H:%M:%S') == MATCH_START_TIME:
            humidity = forecast['main']['humidity']
            weather_main = forecast['weather'][0]['main']
            weather_description = forecast['weather'][0]['description']
            wind_mph = forecast['wind']['speed']
            starting_temp = forecast['main']['feels_like']
            temp_min = forecast['main']['temp_min']
            temp_max = forecast['main']['temp_max']


    status_message_list = [x for x in [check_rain(weather_ids, RAIN_ID),
                               check_heat_rule(starting_temp, HIGH_TEMP_FEELS_LIKE),
                               check_cold_rule(starting_temp, LOW_TEMP_FEELS_LIKE)] if x is not None]

    if len(status_message_list) == 0:
        status = f"OK: Temperature {round(starting_temp)}F/Humidity {humidity}%)"
        print(status)
    elif len(status_message_list) == 1:
        status = f"{status_message_list[0]} (Potential Reschedule)"
        print(status)
    elif len(status_message_list) > 1:
        status_message = " & ".join(status_message_list)
        status = f"{status_message} (Potential Reschedule)"
        print(status)
    else:
        status = f"OK: Temperature {round(starting_temp)}F/Humidity {humidity}%)"


    subject, body = format_weather_email(status, starting_temp, temp_min, temp_max,
                                         humidity, wind_mph, weather_main,
                                         weather_description)




    send_email(subject, body)








