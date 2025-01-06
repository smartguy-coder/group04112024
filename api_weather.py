import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'appid': '47503e85fabbabc93cff28c52398ae97',
    'q': 'Odesa',
    'units': 'metric',
    'lang': 'uk'
}

response = requests.get(url, params=params)
response_json = response.json()

temperature_in_city = response_json['main']['temp']

result = f'Наданий час в місті {params["q"]},температура в повітрі {temperature_in_city}'

print(result)
