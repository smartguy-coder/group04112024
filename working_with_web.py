import requests

url = 'https://dummyjson.com/todos'

params = {
    'limit': 1000,
    'skip': 0
}

response = requests.get(url, params=params)
# content = response.content
# text = response.text
response_json = response.json()

todos = response_json['todos']

completed = 0
for todo in todos:
    if todo['completed']:
        completed += 1

pass
