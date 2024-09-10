import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

response_json = response.json()
# longitude = response_json["iss_position"]["longitude"]
# latitude = response_json["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
print(response_json)