import requests
import json

response = requests.get(
    'https://www.cbr-xml-daily.ru/daily_json.js'
)

data = (response.json())

print(data['Valute']['USD'])

