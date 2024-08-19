path = "C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/"

import json


with open(path + 'data.json', 'r') as data_file:
    data = json.load(data_file)

print(data)