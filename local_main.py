import requests
import datetime

url = 'http://api.openweathermap.org/data/2.5/weather?appid=3aa596c4010eb1744783beac955c8e54&q=Philadelphia,us'
data = requests.get(url).json()

zeroC = 273.15

print "At the moment, in", data['name']
print
print "Temperature:", data['main']['temp']-zeroC,"C"
print "Humidity   :", data['main']['humidity'],"%"
print "Wind speed :", data['wind']['speed']*3.6,"km/h"
print
print data['weather'][0]['description']
print
print "Sunrise:",datetime.datetime.fromtimestamp(data['sys']['sunrise'])
print "Sunset :",datetime.datetime.fromtimestamp(data['sys']['sunset'])
