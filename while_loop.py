my_list = [55, 88]

for item in my_list:
    print(my_list)
    # my_list.append(item)



target_btc_price = 115_000


# while True:
#     current_price = int(input('BTC: '))
#     if current_price >= target_btc_price:
#         print('sold')
#         break


def sell_my_btc_1(target_price: int) -> dict:
    while True:
        current_price = int(input('BTC: '))
        if current_price >= target_price:
            print('sold')
            break
    return {'sold': True, 'price': current_price}

# current_price = 0
#
# flag = True
# while flag:
#     current_price = int(input('BTC: '))
#     if current_price >= target_btc_price:
#         print('sold')
#         flag = False


def sell_my_btc(target_price: int) -> dict:
    while True:
        current_price = int(input('BTC: '))
        if current_price >= target_price:
            print('sold')
            return {'sold': True, 'price': current_price}


# sell_my_btc(target_btc_price)
