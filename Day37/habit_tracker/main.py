import requests
from datetime import datetime

USERNAME = "humblersx"
TOKEN = "dhwaoidfadfadads"
GRAPHID = "graph1"

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
    "id": GRAPHID,
    "name": "My Reading Graph",
    "unit": "chapter",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today_date = datetime.now()
TODAY = today_date.strftime("%Y%m%d")

pixel_config = {
    "date": TODAY,
    "quantity": "1"
}


# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{TODAY}"


update_config = {
    "quantity": "1"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

