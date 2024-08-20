import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

NUTRITION_API_KEY = os.getenv("nutrition_ix_api_key")
NUTRITION_APP_ID = os.getenv("nutrition_ix_app_id")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY
}

sheety_headers = {
    "Authorization": SHEETY_TOKEN
}


params = {
    "query": input("What exercise did you complete?"),
    "weight_kg":59.9,
    "height_cm":175,
    "age":35
}

response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
workout_data = response.json()


# Need to get the following parameters: Date, Time, Exercise, Duration, Calories
now = datetime.now()
today_date = now.strftime("%m/%d/%Y")
current_time = now.strftime("%H:%M:%S")

for idx, exercise in enumerate(workout_data['exercises']):
    exercise_name = workout_data['exercises'][idx]['name']
    duration = workout_data['exercises'][idx]['duration_min']
    calories = round(workout_data['exercises'][idx]['nf_calories'])
    new_row = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=sheety_headers)
    print(response.text)