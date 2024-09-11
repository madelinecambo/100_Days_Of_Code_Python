import requests
import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

# Environment Variables
load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")

# Global Variables
PROMISED_DOWN = 150
PROMISED_UP = 10


#TODO: Create a Class

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url_speed_test = 'https://www.speedtest.net/'
        self.driver.get(url_speed_test)

        go_button = self.driver.find_element(
            by=By.CLASS_NAME,
            value="start-text"
        )
        go_button.click()
        time.sleep(60)

        download_speed = self.driver.find_element(
            by=By.CLASS_NAME,
            value="result-data-large.number.result-data-value.download-speed"
        ).text

        upload_speed = self.driver.find_element(
            by=By.CLASS_NAME,
            value="result-data-large.number.result-data-value.upload-speed"
        ).text

        # return download_speed, upload_speed

        print(f"down: {download_speed}\nup: {upload_speed}")

    def tweet_at_provider(self):
        pass


# bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# bot.tweet_at_provider()

def replace_spaces(input_string: str) -> str:
    return input_string.replace(" ", ".")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

twitter_url = 'https://x.com/i/flow/login'
driver.get(twitter_url)

time.sleep(3)

login_field = driver.find_element(
    by=By.XPATH,
    value='//input[@name="text"]'
)
login_field.send_keys(TWITTER_EMAIL)

time.sleep(2)
next_button = driver.find_element(
    by=By.XPATH,
    value='//span[text()="Next"]'
)

next_button.click()
time.sleep(2)
try:
    password_field = driver.find_element(
        by=By.XPATH,
        value='//input[@type="password"]'
    )
    password_field.send_keys(TWITTER_PASSWORD)

    time.sleep(2)
    login_button = driver.find_element(
        by=By.XPATH,
        value='//span[text()="Log in"]'
    )

    login_button.click()
except:
    print('First Attempt Did not work!')
    username_field = driver.find_element(
        by=By.XPATH,
        value='//input[@name="text"'
    )
    username_field.send_keys(TWITTER_USERNAME)
    time.sleep(2)
    next_button = driver.find_element(
        by=By.XPATH,
        value='//span[text()="Next"]'
    )
    next_button.click()

    time.sleep(2)
    password_field = driver.find_element(
        by=By.XPATH,
        value='//input[@type="password"]'
    )
    password_field.send_keys(TWITTER_PASSWORD)

    time.sleep(2)
    login_button = driver.find_element(
        by=By.XPATH,
        value='//span[text()="Log in"]'
    )

    login_button.click()

tweet_box = driver.find_element(
    by=By.XPATH,
    value='//div[text()="What is happening?!'
)

tweet_box.send_keys("TEST")
