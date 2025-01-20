import requests


URL = 'https://script.google.com/macros/s/AKfycbw549B99KzMVov7-7ERAcnpOD4A6ND9GvlqzYpi5wqP2O-7d3n7Mchq97yI0zwPHTDxlA/exec'


def get_olx_products() -> list[dict]:
    response = requests.get(URL)
    response_json = response.json()
    products = response_json['products']
    return products
