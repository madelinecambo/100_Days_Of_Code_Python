from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/KiiBoom-Swappable-Gasket-Mounted-Mechanical-South-Facing/dp/B0CLTVY3Y6/?_encoding=UTF8&pd_rd_w=kzEGc&content-id=amzn1.sym.255b3518-6e7f-495c-8611-30a58648072e%3Aamzn1.symc.a68f4ca3-28dc-4388-a2cf-24672c480d8f&pf_rd_p=255b3518-6e7f-495c-8611-30a58648072e&pf_rd_r=84PB1MFVANCB1D6QEF4A&pd_rd_wg=K3N3d&pd_rd_r=32a77ebc-90c4-4340-b033-a9ea50c641f6&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1")

# price_dollar = driver.find_element(by=By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(by=By.CLASS_NAME, value="a-price-fraction").text
# print(f"Price is: ${price_dollar}.{price_cents}")

driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# if all other methods fail can use the Xpath

bug_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)


## Challenge: Get a list of upcoming events from Python.org as a dictonary
# dates and names
# format: {0: {'time':'2020-08-28', 'name': 'PyCon JP 2020'}, 1: {'time:'2020-09-05', name

dates = driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget.last ul.menu li time")
event_names = driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget.last ul.menu li a")

# extract text
# dates = [date.text for date in dates]
# event_names = [event_name.text for event_name in event_names]
# create an empty dictionary
python_event_dict = {}

# Fill dictionary
for idx in range(len(dates)):
    python_event_dict[idx] = {
        "time": dates[idx].text,
        "name": event_names[idx].text
    }

print(python_event_dict)


# driver.close()
driver.quit()

