import requests

url = 'https://dummyjson.com/products'

params = {
    'limit': 200,
    'skip': 0
}
response = requests.get(url, params=params)
response_json = response.json()

products = response_json['products']

total_cost_apple_products = 0

for product in products:
    if product.get("brand") == "Apple":
        cost = product["price"] * product["stock"]

        total_cost_apple_products += cost

print(total_cost_apple_products)
