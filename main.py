
from pywebio import start_server
from pywebio.input import input_group, input
from pywebio.output import put_text, put_html, put_success, put_table, put_image, put_button
from pywebio.session import run_js

from google_api import get_olx_products
from utils.email_sender import send_email


def handle_click(product_name: str):
    put_success(f'Вибрано {product_name}')

    data = input_group(
        'Введіть ваші дані',
        [
            input('Ваша електронна пошта', name='email'),
            input('Вашу імя', name='name'),
        ]
    )

    put_success(f'Дякуємо, {data["name"]}')
    send_email([data["email"]], mail_body=product_name, mail_subject='New order')
    run_js('setTimeout( function(){location.reload();}, 2000             )')


def main():
    put_html('<h1>Вітаємо вас на нашому сайті')
    put_success('Товари в наявності')

    products = get_olx_products()

    table = []
    table.append(['№', "Товар", "Ціна, грн", "Опис товару", "Зображення", "Замовити"])

    for idx, product in enumerate(products, start=1):
        product_list = []
        product_list.append(idx)
        product_list.append(product['productName'])
        product_list.append(product['price'])
        product_list.append(product['description'].replace('\t', '')[:81])

        image_url = product['imageURL']
        if image_url:
            image_html = f'<img src="{image_url}" style="width:50px;">'
            product_list.append(put_html(image_html))
        else:
            product_list.append('')

        product_list.append(put_button('Купити', onclick=lambda: handle_click(product['productName'])))

        table.append(product_list)

    put_table(table)


if __name__ == '__main__':
    start_server(main, port=8000, host='127.0.0.1')
