# 100 Days of Code: Day 35 - Keys, Authentication & Environment Variables 

## Project Overview
**Date:** 8/17/2024

**Goal:** 
For Day 35, I gained more experience working with APIs by creating a weather notifier application.

## Project Details
### 1. Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** Requests, smtplib, os (for environment variables)
- **Tools:** PythonAnywhere, Windows Task Scheduler 

### 2. Day Overview 
#### Concepts
- **API Endpoints:** Understanding and utilizing API endpoints for weather data retrieval.
- **Reading API Documentation:** Learning to make API calls with different parameters by reading and interpreting API documentation.
- **Using Keys:** Implementing API keys securely using environment variables.
- **Environment Variables:** Securing sensitive data like API keys and passwords by storing them in environment variables.
- **Program Design:** Designing a weather application that sends email notifications based on weather conditions.

### 3. Day 35 Project - USTA Tennis Team Email Weather App

The main project for Day 35 involved creating a weather application that checks the forecast for the next 12 hours and sends an email if rain is forecasted. I extended this application to check if the "feels like" temperature would exceed the USTA Heat rule (100 degrees) or fall below the USTA cold rule.

#### Project Overview
- **Functionality:** The application retrieves a weather forecast and checks for rain and "feels like" temperatures. If rain is in the forecast or if the USTA temperature rules are violated, the application sends an email informing the recipients about the upcoming conditions. If the weather is favorable, an email is still sent, detailing the good weather and forecasted temperatures at the start of the matches.
  
- **Security:** Environment variables were used to keep API keys, locations, and passwords secure.

- **Deployment:** The application currently runs daily as a scheduled job using Window Task Scheduler. Future improvements will include adding additional functionality, such as a GUI interface to input match dates and the ability to adjust the temperature thresholds that trigger notifications.

### 4. Screenshots 

![image](https://github.com/user-attachments/assets/0bba6b5b-ab9c-4ff9-b308-4be0d1b622a0)



### 5. Tomato Count

Day 35 Lessons and Project took: [🍅🍅🍅🍅][🍅🍅🍅🍅][🍅🍅🍅🍅]
