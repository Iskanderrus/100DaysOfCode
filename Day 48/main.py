# בס״ד
from selenium import webdriver
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha

# connecting webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.amazon.com/errors/validateCaptcha')

# bypassing amazon captcha
# get link to the image
link = driver.find_element(By.XPATH, '//div[@class="a-row a-text-center"]//img').get_attribute('src')
# reading captcha
captcha = AmazonCaptcha.fromlink(link)
captcha_value = AmazonCaptcha.solve(captcha)
# pasting captcha value and clicking the button
driver.find_element(By.ID, 'captchacharacters').send_keys(captcha_value)
driver.find_element(By.CLASS_NAME, 'a-button-text').click()




