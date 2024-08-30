from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# # Navigate to Wikipedia
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Goal: To run the program for 5 min and see if we can get a high score

# cookie = driver.find_element(by=By.ID, value="cookie")
# cookie.click()

start = datetime.datetime.now()
time_interval = 5
print(start)

print(start.second)

seconds = 0

while datetime.datetime.now() < start + datetime.timedelta(seconds=15):
    cookie = driver.find_element(by=By.ID, value="cookie")
    cookie.click()
    if datetime.datetime.now().second - start.second % 5 == 0:
        print('5 seconds has passed!')
        buy_cursor = driver.find_element(By.ID, value="buyCursor")
        buy_cursor.click()


