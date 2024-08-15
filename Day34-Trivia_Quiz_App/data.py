# Get 10 new questions via API call each time the program is run

import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url = "https://opentdb.com/api.php?amount", params=parameters)
response.raise_for_status()

question_data = response.json()['results']

