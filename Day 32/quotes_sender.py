import random
import smtplib
from datetime import datetime as dt

if dt.now().weekday() == 0 and dt.now().hour == 11:
    # setting sending email and password
    my_email = 'alex_ru2002@list.ru'
    with open('../../../Documents/password.txt') as f:
        my_password = f.read()

    # reading the quotes
    with open('data/quotes.txt') as f:
        quotes = f.readlines()

    # getting random author and quote
    quotes_dict = dict()
    for quote in quotes:
        quote, author = quote.split(' - ')
        quotes_dict[author.strip()] = quote.strip()

    author, quote = random.choice(list(quotes_dict.items()))

    with smtplib.SMTP_SSL('smtp.mail.ru') as connection:
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='a.n.chasovskoy@gmail.com',
            msg=f'Subject: {author} for you\n\n\n{quote}'
        )
