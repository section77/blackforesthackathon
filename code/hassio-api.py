import requests

url = "http://192.168.1.102:8123/api/states"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2OTRlMjcyZmZmYzM0YmMzOWE0ZWU3NmU4NmViNzUxNSIsImlhdCI6MTc0NjgyMTg5NywiZXhwIjoyMDYyMTgxODk3fQ.r2Jij93SlvTU61LNilRYC-OuW5gE0mUjgqes5HWmHRI",
}
response = requests.request("GET", url, headers=headers)

print(response.text)