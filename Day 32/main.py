import smtplib

my_email = 'alex_ru2002@list.ru'
with open('../../../Documents/password.txt') as f:
    my_password = f.read()

with smtplib.SMTP_SSL('smtp.mail.ru') as connection:
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='a.n.chasovskoy@gmail.com',
        msg='Subject:Hi there!\n\nThis is the body of my email'
    )

