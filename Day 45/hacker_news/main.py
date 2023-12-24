# בס״ד

import requests
from bs4 import BeautifulSoup
import pandas as pd

# making request
first_page_contents = requests.get(url='https://news.ycombinator.com')
first_page_contents.raise_for_status()

# creating a soup object using request data
soup = BeautifulSoup(first_page_contents.text, features="html.parser")

# selecting all titles with the links and respective resources
headers_links = soup.find_all('span', {'class': 'titleline'})


# getting list of scores
def get_score_if_exists(soup_object, tag, tag_class=None):
    items = soup_object.find_all(name=tag, class_=tag_class)
    scores = []
    for item in items:
        try:
            score = item.find(class_='score').getText().split()[0]
            scores.append(int(score))
        except AttributeError:
            scores.append(0)
    return scores


scores = get_score_if_exists(soup_object=soup,
                             tag='td',
                             tag_class='subtext')

# formatting data for printing and saving to dictionary
articles = []
for x in range(0, len(headers_links)):
    article = dict()
    title = headers_links[x].getText()
    link = headers_links[x].find('a').get('href')
    if 'item?id=' in link:
        link = 'https://news.ycombinator.com/' + link
    # print(f'Title: {title}')
    # print(f"Link: {link}")
    # print()
    article['title'] = title
    article['link'] = link
    article['score'] = scores[x]
    articles.append(article)

data = pd.json_normalize(articles)
top_5_articles = data.sort_values(by=['score'], ascending=False).head(5)
top_5_articles.to_csv('hacker_top5_articles_pg1.csv')