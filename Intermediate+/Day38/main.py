import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 173
AGE = 21

APP_ID = "app_393764ff63ce43a49d7e8b0c"
API_KEY = "nix_live_hcvjIryU21Flv7cLhSHo4yyW17lQ3YGR"

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ceb0323729775afba79b87c7a71a404e/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)