#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, pprint

#Compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
print(location)

#MUST download the json data from OpenWeatherMap.org's API

#MUST load Json data into a Python variable

#               THEREFORE...

#Downloading JSON data from OpenWeatherMap.org's API. %s is the location string thatwill be used in python program
# REFERENCE : https://openweathermap.org/forecast16
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=63262a2b0700cde20e9fe4f03fa7263d' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w= weatherData['list']
#pprint.pprint(w[0])

#displaying the weather
print("Today's Weather in %s:" % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print("Temperature: ", round( (w[0]['main']['feels_like'] - 273.15) * (9/5) + 32, 1 ) )


"""
INSTALLING WITH PIP:
dir: C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64
python -m pip install --user moduleName
"""
