import pandas as pd
import requests
import datetime as dt
from dotenv import load_dotenv
import os
from weather import check_rain, check_cold_rule, check_heat_rule, format_weather_email, send_email
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

# Open Weather API constants
API_KEY = os.getenv("OWM_API_KEY")