import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_FLIGHTS_ENDPOINT")
#https://api.sheety.co/5fe7df6a46acc21933f246a5e23c30d8/flightDeals/prices
SHEETY_TOKEN = os.getenv("SHEETY_FLIGHTS_TOKEN")


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
