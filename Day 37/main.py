# בס״ד
import os

import requests

token = os.environ['PIXELA_TOKEN']
USERNAME = 'iskanderrus'

url = 'https://pixe.la/v1/users'
user_parameters = {
    'token': token,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# # creating user
# response = requests.post(url=url, json=user_parameters)
# print(response.text)

# creating a new graph
graph_url = f'{url}/{USERNAME}/graphs'
headers = {
    'X-USER-TOKEN': token
}
graph_config = {
    'id': f'{USERNAME}01g',
    'name': 'Reading Python Books',
    'unit': 'pg',
    'type': 'int',
    'color': 'ajisai'
}

response = requests.post(url=graph_url, json=graph_config, headers=headers)
print(response.text)
