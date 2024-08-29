


def check_rain(weather_ids, rain_id):
   if (any(x < rain_id for x in weather_ids)):
       return("Forecasted Rain")


def check_heat_rule(starting_temp, USTA_heat):
    if starting_temp >= USTA_heat:
        return(f"USTA Heat Rule Warning")


def check_cold_rule(starting_temp, USTA_cold):
    if starting_temp < USTA_cold:
        return(f"USTA Cold Rule Warning")


def format_weather_email(status, temperature, humidity, wind_speed, weather_main, weather_description):
    subject = f"Tennis Match Weather Alert: {status}"
    body = f"""

    Please find below the weather forecast for today's match.

    Weather Forecast for 6pm:
    - Temperature: {round(temperature)}F
    - Humidity: {humidity}%
    - Wind Speed: {round(wind_speed)} mph
    - General Weather: {weather_main} - {weather_description}

    Please take this forecast into consideration as you prepare for the match. Should the weather conditions be unfavorable, you may want to consider rescheduling the match.

    Good luck!
    """

    return subject, body

