# בס״ד
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
print(data)