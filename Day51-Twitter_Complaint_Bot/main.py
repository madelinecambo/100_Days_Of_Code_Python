import requests
import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        print("Running Speed Test...")
        time.sleep(60)

        download_speed = self.driver.find_element(
            by=By.CLASS_NAME,
            value="result-data-large.number.result-data-value.download-speed"
        ).text

        upload_speed = self.driver.find_element(
            by=By.CLASS_NAME,
            value="result-data-large.number.result-data-value.upload-speed"
        ).text

        self.down = download_speed
        self.up = upload_speed
        print("Speed Test Results:")
        print(f"down: {download_speed}\nup: {upload_speed}\n\n")
        # self.driver.close()

    def tweet_at_provider(self):

        twitter_url = 'https://x.com/i/flow/login'
        self.driver.get(twitter_url)

        time.sleep(3)

        login_field = self.driver.find_element(
            by=By.XPATH,
            value='//input[@name="text"]'
        )
        login_field.send_keys(TWITTER_EMAIL)

        time.sleep(2)
        next_button = self.driver.find_element(
            by=By.XPATH,
            value='//span[text()="Next"]'
        )

        next_button.click()
        time.sleep(2)
        try:
            password_field = self.driver.find_element(
                by=By.XPATH,
                value='//input[@type="password"]'
            )
            password_field.send_keys(TWITTER_PASSWORD)

            time.sleep(2)
            login_button = self.driver.find_element(
                by=By.XPATH,
                value='//span[text()="Log in"]'
            )

            login_button.click()
        except:
            print('First Attempt Did not work!')
            time.sleep(2)
            username_field = self.driver.find_element(
                by=By.XPATH,
                value='//input[@name="text"]'
            )
            username_field.send_keys(TWITTER_USERNAME)
            time.sleep(2)
            next_button = self.driver.find_element(
                by=By.XPATH,
                value='//span[text()="Next"]'
            )
            next_button.click()

            time.sleep(2)
            password_field = self.driver.find_element(
                by=By.XPATH,
                value='//input[@type="password"]'
            )
            password_field.send_keys(TWITTER_PASSWORD)

            time.sleep(2)
            login_button = self.driver.find_element(
                by=By.XPATH,
                value='//span[text()="Log in"]'
            )

            login_button.click()


        time.sleep(5)
        tweet_box = self.driver.find_element(
            by=By.XPATH,
            value='//br[@data-text="true"]'
        )
        content = f"Hey @ATT, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_box.send_keys(content)

        time.sleep(1)
        post_button = self.driver.find_element(
            by=By.XPATH,
            value='//span[text()="Post"]'
        )
        post_button.click()
        post_button.send_keys(Keys.CONTROL, Keys.ENTER)

        tweet_box = self.driver.find_element(
            by=By.XPATH,
            value='//br[@data-text="true"]'
        )

        tweet_box.send_keys(content)
        time.sleep(1)
        post_button = self.driver.find_element(
            by=By.XPATH,
            value='//span[text()="Post"]'
        )
        tweet_box.send_keys(content)
        post_button.click()
        post_button.send_keys(Keys.CONTROL, Keys.ENTER)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()


if (float(bot.down) < PROMISED_DOWN) or (float(bot.up) < PROMISED_UP):
    print("Speed Test Results Less than Contracted speeds. Tweeting at AT&T")
    bot.tweet_at_provider()




