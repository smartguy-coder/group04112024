import requests

url = 'http://api.open-notify.org/astros.json'

params = {}

response = requests.get(url, params=params)
response_json = response.json()

people_in_space = response_json['number']
print(f'{people_in_space=}')
