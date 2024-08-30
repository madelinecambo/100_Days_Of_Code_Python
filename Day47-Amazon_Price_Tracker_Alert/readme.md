# 100 Days of Code: Day 47 - Web Scraping with Headers and Price Monitoring

## Project Overview
**Date:** 8/29/2024

**Goal:** 
For Day 47, I worked on creating a Python bot that checks the price of a product every day at 9 AM and sends an email alert if the price drops below a certain threshold. The focus was on learning to include headers in HTTP requests to improve web scraping success.

## Project Details
### 1. Technologies Used
- **Programming Language:** Python
- **Libraries/Frameworks:** Requests, smtplib
- **Tools:** PyCharm, myhttpheader.com, httpbin.org

### 2. Day Overview 
#### Concepts
- **Headers in HTTP Requests:** Learned to include headers in HTTP requests, which is essential for mimicking a real browser and increasing the chances of successful web scraping.

#### Steps Taken
1. **Viewing Browser Headers:** I used [myhttpheader.com](http://myhttpheader.com/) to see the headers my own browser sends when making requests. This is crucial for understanding how to set up headers for web scraping.
   
2. **Implementing Headers in Requests:**
   - I referred to a Stack Overflow article on [using headers with the Python requests library](https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method) to learn how to pass headers in requests.
   - I added headers to my `main.py` script, including the `User-Agent` and `Accept-Language` headers to mimic a real browser.
   - Additionally, I explored copying the full header from [httpbin.org/headers](https://httpbin.org/headers), excluding sensitive information like the host and `X-Amzn-Trace-id`.

#### Challenges Faced
- **Web Scraping Amazon:** 
  - While I successfully completed the web scraping on a static demo Amazon webpage, I encountered issues with scraping the live Amazon website due to reCAPTCHA. This challenge required more header information and potentially further adjustments to bypass.
  - Due to time constraints, I was unable to complete the live scraping task successfully and had to move on to other work.

### 3. Final Project - Python Bot for Price Monitoring

The main project for the day was developing a Python bot that automates price monitoring on a daily basis, with a focus on learning how to properly set up HTTP request headers for successful web scraping.

#### Project Overview
- **Functionality:** The bot checks the price of a specified product at 9 AM every day and sends an email alert if the price drops below a certain threshold.

- **Headers Implementation:** The project emphasized the importance of including the correct headers in HTTP requests to mimic real browser behavior and improve the chances of successful web scraping.

#### Objective
The objective was to develop a bot capable of daily price monitoring and notification, with a focus on understanding and implementing HTTP request headers for web scraping.

### 4. Screenshots 

![image](https://github.com/user-attachments/assets/6e207885-906b-4220-8826-3be1d1dd8cfb)


### 5. Tomato Count

Day 47 Lessons and Project took: [🍅🍅🍅🍅]
