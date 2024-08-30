# 100 Days of Code: Day 48 - Selenium for Browser Automation

**Date:** 8/30/2024

**Goal:** Learn to use Selenium to automate web browsers for tasks that go beyond simple web scraping, including finding and interacting with elements on a webpage.

**Technologies Used:** 
- **Programming Language:** Python
- **Libraries/Frameworks:** Selenium
- **Tools:** WebDriver, Browser

**Overview:** 
Today, I set up Selenium, a powerful tool for browser automation. Unlike simple HTTP requests, Selenium drives a browser, sending all necessary headers and information to simulate real user interactions. I learned various methods to locate elements on a webpage, including by ID, name, XPath, link text, and CSS selectors. I also explored how to interact with web elements such as input fields and buttons.

**Notes:**
- **Install and Setup Selenium:** 
  - Selenium can be used to automate our browser.
  
- **Finding and Selecting Elements:**
  - Referenced [Selenium documentation](https://selenium-python.readthedocs.io/).
  - Code for loading libraries:
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    ```
  - Selenium allows us to drive a browser, sending all the headers and information that a website like Amazon would expect from a real user.
  - Element Locators include methods like `find_element(By.ID, "id")`, `find_element(By.NAME, "name")`, and `find_element(By.XPATH, "xpath")`.
  - **CSS Selector:** Useful for narrowing down to specific elements.
  - **XPath:** A way of locating specific HTML elements by their path structure.

- **Interacting with Elements:**
  - CSS Selector Method example:
    ```python
    article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a').text
    article_count.click()
    ```
  - Finding elements by link text:
    ```python
    all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
    all_portals.click()
    ```

- **Mini Project:** 
  - Scrape all the upcoming Python events and dates from Python.org.
  - Use multiple element finds with XPath.

**Project:** 
I built a bot to play the Cookie Clicker game. The bot automates clicking the cookie and purchasing upgrades, aiming to achieve a high score by selecting the highest available upgrade every 5 seconds.

**Challenges:** Understanding the differences between element locators and how to best use them in different scenarios. 

**Tomato Count:** [🍅🍅🍅🍅][🍅🍅]
