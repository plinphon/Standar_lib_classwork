import requests
from datetime import datetime
from pprint import pprint

url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok'

result = requests.get(url)
values = result.json()
index = values['hourly']['temperature_2m'].index(max(values['hourly']['temperature_2m']))


date_string = values['hourly']['time'][index]
date_format = "%Y-%m-%dT%H:%M"

date_object = datetime.strptime(date_string, date_format)

print(date_object)