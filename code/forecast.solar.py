import requests, json

# source: https://doc.forecast.solar/api:estimate
z=12
_lat="47.9873"  # latitude of location, -90 (south) … 90 (north); handeled with a precission of 0.0001 or abt. 10 m
_lon="7.7536"   # longitude of location, -180 (west) … 180 (east); handeled with a precission of 0.0001 or abt. 10 m
_dec="60"       # plane declination, 0 (horizontal) … 90 (vertical) - always in relation to the earth's surface; integer
_az="0"         # plane azimuth, -180 … 180 (-180 = north, -90 = east, 0 = south, 90 = west, 180 = north); integer
_kwp=".4"      # installed modules power in kilo watt; float

#      https://api.forecast.solar/estimate/:lat/:lon/:dec/:az/:kwp
url = "https://api.forecast.solar/estimate/"+_lat+"/"+_lon+"/"+_dec+"/"+_az+"/"+_kwp

# result contains:
#  watts: average (?) power for the hours of current and following day
#  watt_hours_period: amount of energy expected for the periods
#  watt_hours: amount of energy expected summed up

print(url)

response = requests.request("GET", url)

response_info = json.loads(response.content)

print(response_info['result']['watt_hours'])

for timestamp, energy in response_info['result']['watt_hours_period'].items():
  print(timestamp, energy)
  