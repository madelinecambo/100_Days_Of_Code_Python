import pandas as pd
import requests
import datetime as dt
from dotenv import load_dotenv
import os
import smtplib
from weather import check_rain, check_cold_rule, check_heat_rule

load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

# Open Weather API constants
API_KEY = os.getenv("OWM_API_KEY")
LAT = os.getenv("MY_LAT")
LON = os.getenv("MY_LON")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LOW_TEMP_FEELS_LIKE = 35
HIGH_TEMP_FEELS_LIKE = 100
RAIN_ID = 700

# Email Related Constants
MY_EMAIL = os.getenv("MyEmail2")
MY_PASSWORD = os.getenv("Email2AppPassword")
TO_EMAIL = os.getenv("MyEmail1")

# Date Constants
TODAY = dt.datetime.now().date()
MATCH_START_TIME = pd.to_datetime(str(TODAY) + ' ' + "18:00")

COMBO_MATCH_DATES = ['2024-08-17', '2024-08-19', '2024-08-26', '2024-09-02', '2024-09-09', '2024-09-16', '2024-09-23']
COMBO_MATCH_DATES = [pd.to_datetime(date) for date in COMBO_MATCH_DATES]
MIXED_MATCH_DATES = pd.date_range('2024-09-14', '2024-11-14', freq='7d').tolist()

if pd.to_datetime(TODAY) in COMBO_MATCH_DATES or TODAY in MIXED_MATCH_DATES:
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
        date_time = forecast['dt_txt']
        if pd.to_datetime(date_time) == MATCH_START_TIME:
            forecast_index = idx
        else:
            forecast_index = 0

    starting_temp = forecast_3hr[forecast_index]['main']['feels_like']

    sms_message = [x for x in [check_rain(weather_ids, RAIN_ID),
                               check_heat_rule(starting_temp, HIGH_TEMP_FEELS_LIKE),
                               check_cold_rule(starting_temp, LOW_TEMP_FEELS_LIKE)] if x is not None]

    if sms_message == 0:
        sms_message = f"The weather conditions are favorable for tonight's matches!\nThe temperature will be {starting_temp} degrees. Have fun!"
        status = f"OK - (Temperature {starting_temp}F)"
        print(status)
    elif len(sms_message) == 1:
        sms_message.append("Matches may need to be rescheduled!")
        sms_message = "\n".join(sms_message)
        status = f"Potential Reschedule (Temperature {starting_temp}F)"
        print(status)
    elif len(sms_message) > 1:
        sms_message.append("Matches may need to be rescheduled!")
        sms_message = "\n".join(sms_message)
        status = f"Potential Reschedule (Temperature {starting_temp}F)"
        print(status)
    else:
        sms_message = f"The weather conditions are favorable for tonight's matches!\nThe temperature will be {starting_temp}F. Have fun!"
        status = "OK - Temperature {starting_temp}F"


    def send_email(sms_message):
        email_subject = f"Tennis Match Status for Tonight: {status}"
        email_message = f"Subject:{email_subject}\n\n{sms_message}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TO_EMAIL,
                                msg=email_message)
        print("Email Sent!")

    send_email(sms_message)








