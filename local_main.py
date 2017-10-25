import requests

zipcode = input("Zip Code: ")
url = 'http://api.openweathermap.org/data/2.5/weather?zip='+str(zipcode)+',us&appid=3aa596c4010eb1744783beac955c8e54'
json_data = requests.get(url).json()

print(json_data)