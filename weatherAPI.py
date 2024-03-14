# Using the Weather API

import requests

weather = requests.get('http://api.weatherapi.com/v1/current.json?key=7f1bbdbd3ebb4f98a93194516241403&q=Atlanta&aqi=no')
json = weather.json()

city = json['location']['name']
state = json['location']['region']

tempInF = json['current']['temp_f']
condition = json['current']['condition']['text']

print('In', city + ',', state, 'it is currently', str(tempInF) + '°F')
print('The condition is', condition)