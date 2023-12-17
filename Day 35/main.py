# בס״ד
import time

import requests

with open('key.txt', 'r') as f:
    API_KEY = f.read().strip()

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

for hour in data['list']:
    # grab all hours and split by days
    if data['list'].index(hour) % 8 == 0:
        print()
    # if weather id less than 700 and time is between 6 am and 4 pm - give a message
    if hour['weather'][0]['id'] < 700 and 16 > int(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(hour['dt'])).split(' ')[1].split(':')[0]) > 6:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(hour['dt'])), ' возьми зонт: ', hour['weather'][0]['description'])
