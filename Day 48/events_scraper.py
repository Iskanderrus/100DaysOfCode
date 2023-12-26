# בס״ד
from selenium import webdriver
from selenium.webdriver.common.by import By

# connecting webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.python.org')

# scraping data to the lists
dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
dates_list = [date.text for date in dates]

names = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
names_list = [name.text for name in names]
links_list = [name.get_attribute('href') for name in names]

# creating the events dataset
events = {dates_list.index(d): {'date': d, 'event': n, 'link': l}
          for d, n, l in zip(dates_list, names_list, links_list)}
print(events)

driver.quit()
