import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import random

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API Endpoints and Keys
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
NEWS_API = 'YOUR_NEWS_API_KEY'

# Stock API Parameters
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

# Date Calculation
today = datetime.now().date()
yesterday = today - timedelta(days=1)
day_before = yesterday - timedelta(days=1)

# Stock Data Request
response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()

# Stock Details Collector
yesterday_close = data['Time Series (Daily)'][f'{yesterday}']['4. close']
day_before_close = data['Time Series (Daily)'][f'{day_before}']['4. close']
difference = float(yesterday_close) - float(day_before_close)
percentage_increase = (difference / float(yesterday_close)) * 100

# News API Parameters
parameters_news = {
    'apiKey': NEWS_API,
    'qInTitle': COMPANY_NAME,
}

# News Data Request
response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
data_news = response_news.json()

# SMS Sender
recovery_code = 'YOUR_TWILIO_RECOVERY_CODE'
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

# Emoji Function
def emoji():
    if percentage_increase > 0:
        return '🔺'
    elif percentage_increase < 0:
        return '🔻'
    else:
        return ''

# Sending Message Function
def sending_message():
    try:
        client = Client(account_sid, auth_token)

        # Check if there are articles available before accessing random index
        if 'articles' in data_news and len(data_news['articles']) > 0:
            random_index = random.randint(0, len(data_news['articles']) - 1)
            title = data_news['articles'][random_index]['title']
            description = data_news['articles'][random_index]['description']

            message_body = f"{STOCK}: {emoji()}{abs(percentage_increase):.2f}% Headline: {title}\nBrief: {description}"
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone_number,
                to='RECIPIENT_PHONE_NUMBER',
            )
        else:
            print("No articles available for sending message.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Execute Sending Message Function
sending_message()
