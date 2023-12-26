# בס״ד
from selenium import webdriver
from selenium.webdriver.common.by import By

# connecting webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

articles_number_en = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text
print(articles_number_en)
driver.quit()