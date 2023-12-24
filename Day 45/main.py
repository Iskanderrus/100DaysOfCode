# בס״ד

from bs4 import BeautifulSoup

with open('website.html', 'r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.name)
print(soup.title.text)
print(soup.title.string)

# possible data types
print(type(soup.title.text))
print(type(soup.title.string))

# getting all a tags
a_tags = soup.find_all(name='a')
for tag in a_tags:
    print(tag.get('href'))
    print(tag.getText())

# getting all p tags
p_tags = soup.find_all('p')
for tag in p_tags:
    print(tag.text)

# isolating a tag by id
heading = soup.find(name='h1', id='name')
print(f'Heading: {heading.text}')

# isolating a tag by class
heading_class = soup.find(name='h3', class_='heading')
print(f'Heading class {heading_class.get("class")[0]}: {heading_class.getText()}')

# using selectors
name = soup.select_one(selector='#name')
print(f'Name: {name.text}')

company_url = soup.select_one(selector='p a')
print(f'Company URL: {company_url.get("href")}')

headings = soup.select(selector='.heading')
print(headings)