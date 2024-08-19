import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = "madelinecambo"
GRAPH_ID = 'graph2'

user_params ={
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# POST: To create a Pixela User Account/Token (Password)
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "100 Days of Python",
    "unit": "tomatoes",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# POST: To create the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# POST a new pixel
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()


post_pixel = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input("How many work sessions (tomatoes) did you complete today?")
}
response = requests.post(url=pixel_creation_endpoint, json=post_pixel, headers=headers)
print(response.text)

# PUT: Update a Pixel
# update_date = datetime(year=2024, month=8, day=19).strftime("%Y%m%d")
# print(update_date)
# update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{update_date}"
#
# update_pixel = {
#     'quantity': '6',
#     'date': update_date
# }
# response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers)
# print(response.text)

# DELETE: deleting a Pixel
# delete_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{update_date}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


