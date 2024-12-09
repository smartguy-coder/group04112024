import decimal

import money
import phrases
import constants


print(phrases.MSG_WELCOME.format(rest=constants.restaurant_name))

total_cost = 0

borsh_quantity = input(phrases.MSG_DISH_OFFER.format(dish='борщ', price=money.borsh_price))
borsh_quantity = int(borsh_quantity)
borsh_price = money.borsh_price * borsh_quantity
# total_cost = total_cost + borsh_price
total_cost += borsh_price

cheese_quantity = input(phrases.MSG_DISH_OFFER.format(dish='синій сир', price=money.cheese_price))
cheese_quantity = int(cheese_quantity)
cheese_price = money.cheese_price * cheese_quantity
total_cost = total_cost + cheese_price

discount_sum = total_cost * constants.discount
discount_sum = decimal.Decimal(str(discount_sum)).quantize(decimal.Decimal('0.01'))

total_to_pay = total_cost - discount_sum

print(phrases.MSG_TOTAL.format(total=total_cost))
print(phrases.MSG_DISCOUNT.format(discount=discount_sum))
print(phrases.MSG_TO_PAY.format(pay=total_to_pay))
