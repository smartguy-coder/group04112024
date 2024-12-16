import decimal

restaurant_name = 'Дача'

discount_from_somewhere = 0.3
discount = decimal.Decimal(str(discount_from_somewhere)).quantize(decimal.Decimal('0.01'))

CURRENT_YEAR = 2024
MIN_DRIVE_AGE = 18
