# בס״ד
import smtplib

import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
# HEADERS = ({'User-Agent':
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Accept-Language': 'ru-RU,ru;q=0.8'})
GOAL_PRICE = 100

response = requests.get(url=URL) # , headers=HEADERS)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, features='html.parser')

try:
    price = float(soup.select_one('div.a-row span.a-price span.a-offscreen').getText().strip('$'))
    product_name = (soup.find(
        name='img',
        class_='a-dynamic-image p13n-sc-dynamic-image p13n-product-image')['alt']
                    .encode('ascii', 'ignore')
                    .decode('ascii')
                    .strip())
except Exception:
    print('Check response or page was changed.')
else:
    if price < GOAL_PRICE:
        with smtplib.SMTP_SSL('smtp.mail.ru') as connection:
            my_email = 'alex_ru2002@list.ru'
            with open('../../../Documents/password.txt') as f:
                my_password = f.read()

            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='a.n.chasovskoy@gmail.com',
                msg=f'Subject: Shopping Time\n\n\n{product_name}\nCheck the page: {URL}\n'
                    f'Current price: ${price}'
            )
