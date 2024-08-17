


def check_rain(weather_ids, rain_id):
   if (any(x < rain_id for x in weather_ids)):
       return("There is rain in the forecast for today.")


def check_heat_rule(starting_temp, USTA_heat):
    if starting_temp >= USTA_heat:
        return(f"The temperature is forecasted to be {starting_temp} at matchtime. USTA heat rule is exceeded.")


def check_cold_rule(starting_temp, USTA_cold):
    if starting_temp < USTA_cold:
        return(f"The temperature is forecasted to be {starting_temp} at matchtime. USTA cold rule is exceeded.")


