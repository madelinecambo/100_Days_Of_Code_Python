from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

# Load Environment Variables
ENVIRONMENT_PATH = "C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/"
load_dotenv(f"{ENVIRONMENT_PATH}.env.txt")
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# URL to LinkedIn Easy Apply Jobs

url = ('https://www.linkedin.com/jobs/search/?currentJobId=3983197980&distance=25&f_AL'
       '=true&f_E=3%2C4&geoId=90000664&keywords=Data%20Scientist&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true')

# linkedin_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3983197980&distance=25&f_AL'
#                 '=true&f_E=3%2C4&geoId=90000664&keywords=Data%20Scientist&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true'

#  Navigate LinkedIn Easy Apply Jobs Webpage
driver.get(url)
time.sleep(10)

# Sign into LinkedIn
# locate signin button and click
signin_button = driver.find_element(
    by=By.CLASS_NAME,
    value="nav__button-secondary.btn-md.btn-secondary-emphasis"
)
signin_button.click()

# Delay by 5 seconds to allow page to load
time.sleep(2)

# Fill in Information for Username and Password
username_field = driver.find_element(by=By.ID, value="username")
username_field.send_keys(LINKEDIN_USERNAME)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(LINKEDIN_PASSWORD)
# Click the sign on button after information is entered
signin_blue_button = driver.find_element(
    by=By.CLASS_NAME,
    value="btn__primary--large.from__button--floating")
signin_blue_button.click()

# Click LinkedIn Easy Apply Button for First Job
easy_apply_button = driver.find_element(by=By.CSS_SELECTOR,
                                        value=".jobs-s-apply span.artdeco-button__text")
easy_apply_button.click()

time.sleep(1)
next_button = driver.find_element(
    by=By.CSS_SELECTOR,
    value='.jobs-easy-apply-content span.artdeco-button__text'
)
next_button.click()

time.sleep(1)
next_button_2 = driver.find_element(
    by=By.CSS_SELECTOR,
    value='span.artdeco-button__text'
)
next_button_2.click()

linkedin_profile_field = driver.find_element(
    by=By.CSS_SELECTOR,
    value='.single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3983197980-2525502825-text'
)
linkedin_profile_field.send_keys("https://www.linkedin.com/in/madeline-cambo-2b911445/")

website_field = driver.find_element(
    by=By.CSS_SELECTOR,
    value='.single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3983197980-2525502817-text'
)
github = "https://github.com/madelinecambo"
website_field.send_keys(github)

# Click Review Button
review_button = driver.find_element(
    by=By.CSS_SELECTOR,
    value='#ember722 span'
)
review_button.click()
time.sleep(1)

# Submit Application
submit_button = driver.find_element(
    by=By.CSS_SELECTOR,
    value='#ember734 span'
)
submit_button.click()












