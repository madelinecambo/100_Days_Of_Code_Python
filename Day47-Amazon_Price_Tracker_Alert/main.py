import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

# Environment Variables
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")
MY_EMAIL = os.getenv("MyEmail2")
MY_PASSWORD = os.getenv("Email2AppPassword")
TO_EMAIL = os.getenv("MyEmail1")

practice_url = "https://appbrewery.github.io/instant_pot/"
TARGET_PRICE = 100

HEADER = {"Accept-Language":"en-US"}

# GOAL: get the price as a floating point number
# <div class="a-section a-spacing-none aok-align-center aok-relative">
# <span class="aok-offscreen"> $99.99 </span>

# Make an HTTP GET request to the webpage
response = requests.get(url=practice_url, headers = HEADER)

# Extract webpage text
webpage_text = response.text
# Turn Text into Soup
soup = BeautifulSoup(webpage_text, "html.parser")

# Use find method on the Soup to extract the section with the current price
section = soup.find(name="div",
                    class_="a-section a-spacing-none aok-align-center aok-relative")

# tap into the section to extract the price
# get the text, Split off $, and convert to a float
current_price = (float(section
                       .find(name="span", class_="aok-offscreen")
                       .getText()
                       .strip()
                       .split("$")[1])
                 )

print(current_price)

def send_email(subject, body):
    email_message = f"Subject:{subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=email_message)
    print("Email Sent!")

if current_price < TARGET_PRICE:
    subject = "Insta Pot Price Alert!"
    body = f"The product price is now ${current_price}, below your target price. Buy now!"

    send_email(subject, body)


