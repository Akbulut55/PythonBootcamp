
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
weather_params = {
    "lat": 0,
    "lon": 0,
    "appid": "yourid"
}

import requests
response = requests.get(OWM_endpoint, params=weather_params)
# print(response.status_code)
data = response.json()
for x, hour_data in enumerate(data["list"]):
    weather_id = hour_data["weather"][0]["id"]
    if x > 4:
        break
    elif weather_id < 700:
        print("Bring an umbrella.")
        break
