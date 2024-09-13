import requests
from datetime import datetime

USERNAME = "YourUserName"
TOKEN = "YourToken"
GRAPH_ID = "SomeGraph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Productivity Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ichou",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)

graph_post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()

graph_post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes were you productive today?"),
}

# response = requests.post(graph_post_pixel_endpoint, json=graph_post_pixel_config, headers=headers)

update_endpoint = f"{graph_post_pixel_endpoint}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "111.8"


}

# response = requests.put(update_endpoint, headers=headers, json=new_pixel_data)

delete_endpoint = f"{graph_post_pixel_endpoint}/{today.strftime("%Y%m%d")}"

response = requests.delete(delete_endpoint, headers=headers)
print(response.text)
