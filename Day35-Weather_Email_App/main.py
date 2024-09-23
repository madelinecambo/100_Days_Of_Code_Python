import pandas as pd
import requests
import datetime as dt
from dotenv import load_dotenv
import os
from weather import check_rain, check_cold_rule, check_heat_rule, format_weather_email, send_email
import openpyxl

load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

# Open Weather API constants
API_KEY = os.getenv("OWM_API_KEY")
LAT = os.getenv("MY_LAT")
LON = os.getenv("MY_LON")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LOW_TEMP_FEELS_LIKE = 35
HIGH_TEMP_FEELS_LIKE = 100
RAIN_ID = 700

# Read in Match Dates
TENNIS_INPUT_PATH = r"C:\Users\madel\OneDrive\Projects\USTA_Tennis_Software\Weather Alert App"
matches = pd.read_excel(TENNIS_INPUT_PATH + "/match_input_file.xlsx", parse_dates=True)
TODAY = dt.datetime.now().date()
today_match = matches[matches.Date == str(TODAY)]

if len(today_match) > 0:
    print('There is a match today!')
    weather_forecast_time = today_match.iloc[0].Time
    match_start_time = today_match.iloc[0].Time.strftime("%I:%M %p")

    match_location = today_match.iloc[0].Location
    match_league = today_match.iloc[0].League

    if str(weather_forecast_time) == '19:00:00':
        weather_forecast_time = pd.to_datetime(str(TODAY) + ' ' + "18:00:00").strftime('%H:%M:%S')
    else:
        weather_forecast_time = weather_forecast_time.strftime('%H:%M:%S')

    parameters = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "cnt": 5,
        "units": 'imperial'
    }
    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    response.raise_for_status()

    forecasts_json = response.json()

    weather_ids = []
    forecast_3hr = forecasts_json['list']
    weather_forecast_datetime = pd.to_datetime(str(TODAY) + ' ' + weather_forecast_time).strftime('%Y-%m-%d %H:%M:%S')
    relevant_forecast = []

    for idx, forecast in enumerate(forecast_3hr):
        if pd.to_datetime(forecast['dt_txt']) <= pd.to_datetime(weather_forecast_datetime):
            relevant_forecast.append(forecast)


    for idx, forecast in enumerate(relevant_forecast):
        weather_ids.append(forecast['weather'][0]['id'])
        print(forecast)
        print(weather_forecast_time)
        if pd.to_datetime(forecast['dt_txt']).strftime('%H:%M:%S') == weather_forecast_time:
            print('This worked!')
            forecast_start_time = pd.to_datetime(forecast['dt_txt']).strftime("%I:%M %p")
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
        status = f"OK- Temperature {round(starting_temp)}F/ Humidity {humidity}%"
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

    subject = f'Weather Forecast Alert: {status}'

    body = format_weather_email(subject, status, starting_temp, temp_min, temp_max,
                                         humidity, wind_mph, weather_main,
                                         weather_description, match_league,
                                        match_start_time, match_location,
                                        weather_forecast_time=forecast_start_time)

    send_email(subject, body)
