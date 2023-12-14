# בס״ד
import datetime
import smtplib
import time

import requests

while True:
    # get local sunset and sunrise time in 24h format
    url = 'https://api.sunrise-sunset.org/json'
    parameters_su = {
        'lat': 46.104495,
        'lon': 19.663891,
        'date': (datetime.datetime.now() + datetime.timedelta(1)).strftime('%Y-%m-%d'),
        'formatted': 0
    }

    response = requests.get(url=url, params=parameters_su)
    response.raise_for_status()
    su_sunrise = int(response.json()['results']['sunrise'].split('T')[1].split(':')[0])
    su_sunset = int(response.json()['results']['sunset'].split('T')[1].split(':')[0])

    # getting current position of the ISS
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    # iss position
    iss_position = data['iss_position']
    iss_lon = float(iss_position['longitude'])
    iss_lat = float(iss_position['latitude'])

    current_hour = datetime.datetime.now().hour
    if (su_sunrise > current_hour > su_sunset) and (45.5 < iss_lat < 46.5) and (19 < iss_lon < 20):
        my_email = 'alex_ru2002@list.ru'
        with open('../../../Documents/password.txt') as f:
            my_password = f.read()

        with smtplib.SMTP_SSL('smtp.mail.ru') as connection:
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='a.n.chasovskoy@gmail.com',
                msg=f'Subject: ISS is close\n\n\nLook high into the sky! '
                    f'Current ISS position is:\nlatitude: {iss_lat}\nlongitude: {iss_lon}'
            )
    time.sleep(60)
