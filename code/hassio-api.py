import requests

url = "http://192.168.1.102:8123/api/states"
headers = {
    "Authorization": "Bearer <token>",
}
response = requests.request("GET", url, headers=headers)

print(response.text)