# בס״ד
import os
import time

import requests

from twilio.rest import Client

# twilio credentials
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
US_PHONE_NUMBER = os.environ.get('US_PHONE_NUMBER')

# openweather credentials
API_KEY = os.environ.get('OWM_API_KEY')


# weather forecast for the next 5 days - forested for every 3 hours
url = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': 46.104495,
    'lon': 19.663891,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()

data = response.json()
# use only next 12 hours
for hour in data['list'][0:5]:
    # grab all hours and split by days
    condition_code = hour['weather'][0]['id']
    hour_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(hour['dt'])).split(' ')[1].split(':')[0]
    forecast_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(hour['dt']))
    description = hour['weather'][0]['description']

    if data['list'].index(hour) % 8 == 0:
        print()
    # if weather id less than 700 and time is between 6 am and 4 pm - give a message
    if (condition_code < 700 and
            16 > int(hour_str) > 6):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f'Take an umbrella. It is {description} today ☔',
            from_=US_PHONE_NUMBER,
            to='+381629448617'
        )
        print(message.status)