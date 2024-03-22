# Using the Weather API

import requests

city = input('What city would you like the weather for?\n')

weather = requests.get('http://api.weatherapi.com/v1/current.json?key=7f1bbdbd3ebb4f98a93194516241403&q=' + city + '&aqi=no')
json = weather.json()

city = json['location']['name']
region = json['location']['region']
country = json['location']['country']

tempInF = json['current']['temp_f']
condition = json['current']['condition']['text']

print('In', city + ',', region + ',', country, 'it is currently', str(tempInF) + '°F')
print('The condition is', condition)    