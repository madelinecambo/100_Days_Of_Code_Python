import requests
from dotenv import load_dotenv
import os

load_dotenv("C:/Users/madel/OneDrive/Projects/PythonEnvironmentVariables/.env.txt")
from message import generate_header, send_email, percent_difference

STOCK_NAME = "CRMD"
COMPANY_NAME = "CorMedix Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "pageSize": 3,
}

# Email Related Constants
MY_EMAIL = os.getenv("MyEmail2")
MY_PASSWORD = os.getenv("Email2AppPassword")
# TO_EMAIL = os.getenv("MOM_EMAIL")
TO_EMAIL = os.getenv("MyEmail1")

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

stock_data_list = [value for (key, value) in stock_data['Time Series (Daily)'].items()]

close_price_yesterday = float(stock_data_list[0]['4. close'])

# Get the day before yesterday's closing stock price
close_price_day_before_yesterday = float(stock_data_list[1]['4. close'])

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
closing_price_difference = percent_difference(close_price_yesterday, close_price_day_before_yesterday)

# If TODO4 percentage is greater than 5 then print("Get News").

if closing_price_difference == 0:
    print("Get News!")

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    formatted_articles = [f"Headline: {article['title'].encode('ascii', 'ignore').decode("utf-8")}.\nBrief: {article['description'].encode('ascii', 'ignore').decode("utf-8")}"
                          for article in news_data['articles']]

    if closing_price_difference > 0:
        symbol = "+"
    else:
        symbol = "-"

    header = generate_header(symbol, STOCK_NAME, closing_price_difference)

    full_email_message = header + "\n".join(formatted_articles)

    send_email(header, full_email_message)
