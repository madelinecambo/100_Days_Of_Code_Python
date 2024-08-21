# 100 Days of Code: Day 38 - Workout Tracker

## Project Overview
**Date:** 8/19/2024

**Goal:**  
 For today's project I built a Workout Tracker. The program will ask the user which workouts were completed today and will extract information from the user's answer and put it in a Google Sheet.

## Project Details
### 1. Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** requests, datetime, os, dotenv
- **Tools:** PyCharm and Jupyter Notebooks

### 2. Project Description

For today's project I built a Workout Tracker. 
The workout tracker uses the following APIs:
- Sheety https://sheety.co/docs/authentication.html
    - For extracting the information from the Python script and putting the data into the Google Sheet
- Nutritionix https://docx.syndigo.com/developers/docs/getting-started-1
    - For natural language processing. The Nutritionix API takes in the user's activity description and will return duration, calories, and exercise name

Leveraging those two endpoints I was able to create a program for user's to enter in their daily activity. 
The daily activities will be passed to the Nutritionix API, which will return a json object with all the relevant data for Exercise Tracking.
This data will then be passed (for each exercise entered by the user) into the Sheety API which will put the data into the Workouts Google sheet.

### 3. Screenshots 

![image](https://github.com/user-attachments/assets/d1da2e8f-6842-481f-a624-53fc6bae26c4)

### 4. Tomato Count

This project took: 🍅🍅

