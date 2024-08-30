from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# # Navigate to Wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# XPATH method
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text


# CSS Selector Method - Uses the ID field
# article_count = driver.find_element(By.CSS_SELECTOR,
#                                     value='#articlecount a').text

# to click the link -> brings us to stats page
# article_count.click()


# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

# Challenge - Fill out form to sign up for newsletter

# Navigate to Newsletter form
driver.get("https://secure-retreat-92358.herokuapp.com/")

# first name field
first_name_field = driver.find_element(By.CSS_SELECTOR, value=".form-control.top")
first_name_field.send_keys("Madeline")
last_name_field = driver.find_element(By.CSS_SELECTOR, value=".form-control.middle")
last_name_field.send_keys("Cambo")
email_field = driver.find_element(By.CSS_SELECTOR, value=".form-control.bottom")
email_field.send_keys("madelineann11@gmail.com")

signup_button = driver.find_element(By.TAG_NAME, value="button")
signup_button.click()
