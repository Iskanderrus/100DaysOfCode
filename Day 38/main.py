# בס״ד
import datetime
import os

import requests
from datetime import datetime

# personal data
GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

# Nutritionix credentials
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

#
BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
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
result = response.json()

# adding data to a spreadsheet
current_date = datetime.now().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H:%M:%S')

bearer_headers = {
    "Authorization": BEARER_TOKEN
}

sheet_url = 'https://api.sheety.co/63f4849df2c2706c138bb26316b12333/myWorkouts/workouts'
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_url, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
