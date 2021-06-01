import requests
from datetime import datetime
import os

# APP ID AND KEY FOR NUTRITIONIX

NUTRIONIX_APP_ID = "6b75133b"
API_KEY_NUTRIONIX = os.environ['API_KEY_NUTRIONIX']
SHEETY_USERID = "f0b2e84905e64f22023d297978a9331c"

# USER DATA

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 178
AGE = 26

# API DECLARATION

NUTRIONIX_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = f"https://api.sheety.co/{SHEETY_USERID}/myWorkouts/workouts"


query_text = input("Enter your Data: ").lower()

# NUTRIONIX API PARAMS AND HEADERS

api_headers = {
    "x-app-id": NUTRIONIX_APP_ID,
    "x-app-key": API_KEY_NUTRIONIX,
}

user_params = {
    "query": f"{query_text}",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# NUTRIONIX API INITIALIZATION AND DATA UPDATE USING HTTP POST

response = requests.post(url=NUTRIONIX_API, json=user_params, headers=api_headers)
result = response.json()

# SHEETY HEADERS

SHEETY_AUTH_TOKEN = os.environ['SHEETY_AUTH_TOKEN']

sheety_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# TODAY'S DATE AND TIME

now = datetime.now()
today = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M")

# IMPORTING DATA FROM NUTRIONIX API TO SHEETY SHEET's

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_API, json=sheet_inputs, headers=sheety_header)

    # https://docs.google.com/spreadsheets/d/1NC4EjDO4LsmI9VZIfe_yhH04i8lcrUgLy1TiKeZoH8k/edit#gid=0

    print(sheet_response.status_code)
