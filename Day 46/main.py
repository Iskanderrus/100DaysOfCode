# בס״ד
import requests
from bs4 import BeautifulSoup

#date = input('Which date do you want travel to?\nType date in format: YYYY-MM-DD\n')
URL = f'https://www.billboard.com/charts/hot-100/1980-08-30'

response = requests.get(url=URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, features='html.parser')
hits = soup.find_all(name='ul', class_='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max')
songs = []
#singers = []
for hit in hits:
    songs.append(hit.find('h3').text.strip())
    #singers.append(hit.find('span').text.strip())

