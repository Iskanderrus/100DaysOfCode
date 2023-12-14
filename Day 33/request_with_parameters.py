# בס״ד
import datetime
import requests

url = 'https://api.sunrise-sunset.org/json'
parameters_su = {
    'lat': 46.104495,
    'lon': 19.663891,
    'date': datetime.datetime.now().strftime('%Y-%m-%d')
}

parameters_bu = {
    'lat': 44.800902,
    'lon': 44.158869,
    'date': datetime.datetime.now().strftime('%Y-%m-%d')
}

response = requests.get(url=url, params=parameters_su)
response.raise_for_status()
su_sunrise = response.json()['results']['sunrise']
su_sunset = response.json()['results']['sunset']
print(f'Sunrise in Su: {su_sunrise}')
print(f'Sunset in Su: {su_sunset}')

response = requests.get(url=url, params=parameters_bu)
response.raise_for_status()
bu_sunrise = response.json()['results']['sunrise']
bu_sunset = response.json()['results']['sunset']
print(f'Sunrise in Bu: {bu_sunrise}')
print(f'Sunset in Bu: {bu_sunset}')
