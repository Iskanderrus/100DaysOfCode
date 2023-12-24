# בס״ד

import requests
from bs4 import BeautifulSoup

# scraping data
url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
soup = BeautifulSoup(requests.get(url=url).text, features='html.parser')

# extracting titles to the list and reverse order
titles = reversed([title.text for title in soup.find_all(name='h3', class_='title')])

# write the data to the file
with open('top100_movies.txt', 'w') as file:
    file.write('\n'.join(titles))
