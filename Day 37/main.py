# בס״ד
import os

import requests

token = os.environ['PIXELA_TOKEN']

# creating user
url = 'https://pixe.la/v1/users'
user_parameters = {
    'token': token,
    'username': 'iskanderrus',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

response = requests.post(url=url, json=user_parameters)
print(response.text)
