import requests
from datetime import datetime

USERNAME = "yourname"
TOKEN = "yourtoken"
GRAPH_ID = "yourid"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "yourid",
    "name": "name",
    "unit": "Min",
    "type": "float",
    "color": "momiji"
}

graph_update = {
    "name": "name",
    "unit": "Hour",
    "color": "momiji",
    "timezone": "yourtimezone"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# any_date = datetime(year=2020, month=7, day=23)
today = (datetime.now()).strftime("%Y%m%d")

pixel_creation_data = {
    "date": today,
    "quantity": "64.0"
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today}"

pixel_update_data = {
    "quantity": "83"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)

pixel_add_endpoint = f"{graph_endpoint}/{GRAPH_ID}/add"

pixel_add_data = {
    "quantity": "50"
}

response = requests.put(url=pixel_add_endpoint, json=pixel_add_data, headers=headers)
print(response.text)

# response = requests.put(url=pixel_creation_endpoint, json=graph_update, headers=headers)
# print(response.text)
