# בס״ד
import os
import time
from datetime import datetime

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
    'X-USER-TOKEN': token,
}
# graph_config = {
#     'id': f'{USERNAME}01g',
#     'name': 'Reading Python Books',
#     'unit': 'pg',
#     'type': 'int',
#     'color': 'ajisai'
# }
#
# response = requests.post(url=graph_url, json=graph_config, headers=headers)

# adding a pixel to the graph
today = datetime.now().strftime('%Y%m%d')

python_books_url = f'{graph_url}/{USERNAME}01g'

# python_graph_config = {
#     'date': today,
#     'quantity': '5',
# }
#
# response = requests.post(url=python_books_url, json=python_graph_config, headers=headers)
# while response.json()['message'] != 'Success.':
#     response = requests.post(url=python_books_url, json=python_graph_config, headers=headers)
#     print(response.text)
#     time.sleep(5)

# updating existing pixel
put_url = f'{python_books_url}/{today}'

put_json = {
    'quantity': '2',
}

response = requests.put(url=put_url, json=put_json, headers=headers)
print(f'Update completed: {response.text}')

# deleting existing pixel
response = requests.delete(url=put_url, headers=headers)

print(f'Pixel deleted: {response.text}')

