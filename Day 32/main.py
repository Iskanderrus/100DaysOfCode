import smtplib

my_email = 'alex_ru2002@list.ru'
with open('../../../Documents/password.txt') as f:
    my_password = f.read()

connection = smtplib.SMTP_SSL('smtp.mail.ru')
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs='a.n.chasovskoy@gmail.com', msg='Hi there!')
connection.close()
