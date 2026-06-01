# Pixela
import requests

TOKEN = "TOKEN_NAME"
USERNAME = "ID_USERNAME"
GRAPH_ID = "GRAPH"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create user account
#response = requests.post(pixela_endpoint,json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "running graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#Create a Graph
#response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

#graph link = https://pixe.la/v1/users/zeus243/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20260302",
    "quantity": "8"
}

# response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

#Update a Graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_data['date']}"

new_pixel_data = {
    "quantity": "5"
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

#Delete a Graph
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixel_data['date']}"

response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)
