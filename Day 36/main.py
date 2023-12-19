# בס״ד
import os
from datetime import datetime, timedelta

import requests
from newsapi import NewsApiClient
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# twilio credentials
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
US_PHONE_NUMBER = os.environ.get('US_PHONE_NUMBER')

# other API keys
stock_key = os.environ['ALPHA_VANTAGE_API_KEY']
news_key = os.environ.get('NEWS_API_KEY')

# getting yesterday and day before yesterday dates
yesterday = datetime.now() - timedelta(1)
day_before_yesterday = datetime.now() - timedelta(2)

# handling weekend
yesterday_weekno = yesterday.weekday()
day_before_yesterday_weekno = day_before_yesterday.weekday()

if yesterday_weekno == 5:
    yesterday = yesterday - timedelta(1)
elif yesterday_weekno == 6:
    yesterday = yesterday - timedelta(2)

if day_before_yesterday_weekno == 5:
    day_before_yesterday = day_before_yesterday - timedelta(1)
elif day_before_yesterday_weekno == 6:
    day_before_yesterday = day_before_yesterday - timedelta(2)

yesterday = str(yesterday).split(' ')[0]
day_before_yesterday = str(day_before_yesterday).split(' ')[0]

# requesting market data
url = 'https://www.alphavantage.co/query'
parameters = {
     'function': 'TIME_SERIES_DAILY',
     'symbol': STOCK,
     'apikey': stock_key
}
r = requests.get(url, params=parameters)
r.raise_for_status()
data = r.json()

# getting closing price
yesterday_close = float(data['Time Series (Daily)'][yesterday]['4. close'])
day_before_yesterday_close = float(data['Time Series (Daily)'][day_before_yesterday]['4. close'])

price_difference = abs(round(100-(yesterday_close/day_before_yesterday_close * 100), 2))

# if price difference is over 5%, getting the news and sending three news titles and brief descriptions and links
if price_difference >= 5:
    newsapi = NewsApiClient(api_key=news_key)
    all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                          from_param=day_before_yesterday)

    articles = all_articles['articles'][:3]
    for article in articles:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f'{article["title"]}\n{article["description"]}\n{article["url"]}',
            from_=US_PHONE_NUMBER,
            to='+381629448617'
        )
        print(message.status)
