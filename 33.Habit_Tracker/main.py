import requests
from datetime import date

TOKEN = "hahahahahahaha"
USERNAME = "rohit"
GRAPH_ID = "graph12"

# DEFINING PIXELA API AND PARAMETERS

pixela_api = "https://pixe.la/v1/users/"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CALLING API TO CREATE PIXELA ACCOUNT(https://pixe.la/@rohit) AND CHECKING RESPONSE

# response = requests.post(url=pixela_api, json=user_params)
# print(response.text)

# CREATING GRAPH USING API & HTTP POST

graph_api = f"{pixela_api}{USERNAME}/graphs"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph12",
    "name": "Habit Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

# CREATES A GRAPH(https://pixe.la/v1/users/rohit/graphs/graph12.html) THROUGH THE API

# response = requests.post(url=graph_api, json=graph_params, headers=graph_headers)
# print(response.text)

# POSTING DATA TO THE GRAPH USING HTTP POST

today = date.today()
format_today = today.strftime("%Y%m%d")

graph_data_api = f"{pixela_api}{USERNAME}/graphs/{GRAPH_ID}"

graph_data_params = {
    "date": format_today,
    "quantity": "1",
}

# response = requests.post(url=graph_update_api, json=graph_update_params, headers=graph_headers)
# print(response.text)

# UPDATE GRAPH FOR PAST DATA USING HTTP PUT

graph_update_api = f"{pixela_api}{USERNAME}/graphs/{GRAPH_ID}/{format_today}"

graph_update_params = {
    "quantity": "100",
}

# response = requests.put(url=graph_update_api, json=graph_update_params, headers=graph_headers)
# print(response.text)

# DELETE GRAPH DATA USING HTTP DELETE

response = requests.delete(url=graph_update_api, headers=graph_headers)
print(response.text)

