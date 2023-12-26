# בס״ד
import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# connecting webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.delete_all_cookies()
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# find element by selector and click it
# articles_number_en = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# articles_number_en.click()

# find link by it's name and click it
# all_portals = driver.find_element(By.LINK_TEXT, 'other Wikipedias are available')
# all_portals.click()

# performing search
# search_field = driver.find_element(By.NAME, 'search')
# search_field.send_keys('Australia')

# Option 1
# search_button = driver.find_element(By.CLASS_NAME, 'cdx-search-input__end-button')
# search_button.click()

# Option 2
# search_field.send_keys(Keys.ENTER)
# driver.quit()

# getting website name and credentials from the file
path = Path('../../../Documents/password_manager_log.json')
with open(path, 'r') as file:
    contents = json.load(file)
website = list(contents.keys())[0]
username = contents[website]['username']
password = contents[website]['password']
website = f'https://{website}/login.aspx'

driver.get(website)

# getting the fields to fill
user_name_field = driver.find_element(By.NAME, 'ctl00$mainContent$c_loginForm$m_email')
password_field = driver.find_element(By.NAME, 'ctl00$mainContent$c_loginForm$m_password')
# entering the credentials
user_name_field.send_keys(username)
password_field.send_keys(password)
button = driver.find_element(By.NAME, 'ctl00$mainContent$c_loginForm$m_loginSubmit')
button.click()
driver.refresh()
