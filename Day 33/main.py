# בס״ד

import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
# print the response code
print(response.status_code)
# raise an error message in case connection is not successful
response.raise_for_status()
# print the response json
data = response.json()
print(data)

# iss position
iss_position = data['iss_position']
print(iss_position)