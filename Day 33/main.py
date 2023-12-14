import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
# print the response code
print(response)
# print the response json
print(response.json())
