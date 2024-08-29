import smtplib
import os
from dotenv import load_dotenv
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")
# Email Related Constants
MY_EMAIL = os.getenv("MyEmail2")
MY_PASSWORD = os.getenv("Email2AppPassword")
TO_EMAIL = os.getenv("MyEmail1")

def check_rain(weather_ids, rain_id):
   if (any(x < rain_id for x in weather_ids)):
       return("Forecasted Rain")


def check_heat_rule(starting_temp, USTA_heat):
    if starting_temp >= USTA_heat:
        return(f"USTA Heat Rule Warning")


def check_cold_rule(starting_temp, USTA_cold):
    if starting_temp < USTA_cold:
        return(f"USTA Cold Rule Warning")


def format_weather_email(status, temperature, temp_min, temp_max, humidity, wind_speed, weather_main, weather_description):
    subject = f"Tennis Match Weather Alert: {status}"
    body = f"""

Please find below the weather forecast for today's match.

Weather Forecast for 6pm:
- Temperature (Feels Like): {round(temperature)}F
- Actual Temperature: {round(temp_min)}F - {round(temp_max)}F
- Humidity: {humidity}%
- Wind Speed: {round(wind_speed)} mph
- General Weather: {weather_main} - {weather_description}

Please take this forecast into consideration as you prepare for the match. \n\nShould the weather conditions be unfavorable, you may want to consider rescheduling the match.

Good luck!
    """

    return subject, body

def send_email(subject, body):
    email_message = f"Subject:{subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=email_message)
    print("Email Sent!")

