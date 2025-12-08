import requests

# Nutrition API
APP_ID = "APP_ID"
API_KEY = "API_KEY"
GENDER = "male"
WEIGHT_KG = 87
HEIGHT_CM = 180
AGE = 46
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpint = "https://api.sheety.co/648d7c42ea0cdc67595ede1e75f59b24/myWorkoutsHumblersx/workouts"
exercise_text = input("What exercise did you do today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    }


parameters = {
    "workout": {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")



response = requests.post(url=sheety_endpint, json=parameters)
result = response.json()
print(result)

# response = requests.get(exercise_endpoint, params=user_params)
# print(response)