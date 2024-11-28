import decimal

# print(round(1.5, 0))
# print(round(2.5, 0))
# print(decimal.Decimal(str(1.5)).quantize(decimal.Decimal('0.')))
# print(decimal.Decimal(str(2.5)).quantize(decimal.Decimal('0.')))

cheese_price_from_somewhere = 133.3301
cheese_price = decimal.Decimal(str(cheese_price_from_somewhere)).quantize(decimal.Decimal('0.01'))

botsh_price_from_somewhere = 80
borsh_price = decimal.Decimal(str(botsh_price_from_somewhere)).quantize(decimal.Decimal('0.01'))
