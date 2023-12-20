# בס״ד

import os

import requests

# personal data
GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

# Nutritionix credentials
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

# request data
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": input("Tell me which exercises you did:\n"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# making request
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()['exercises'][0]

# extracting data
print(f"Duration: {result['exercises'][0]['duration_min']}")
print(f"Calories burned: {result['exercises'][0]['nf_calories']}")
print(f"Correct name: {result['exercises'][0]['name']}")
