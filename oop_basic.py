import datetime as dt
from typing import Self


class Person:


    def __init__(self, first_name: str, surname: str):
        self.name = first_name
        self.surname = surname

        now = dt.datetime.now()
        self.birthday = now.replace(year=2000)
        self.money = 0


    def beg_money(self, amount: int):
        self.money += amount
        # text = 'jkhjhk'.replace('h', 'a').replace('d', '1')
        return self

    def __str__(self) -> str:
        return f'<{self.name} with {self.money}grn>'

    def lend_money(self, other: Self, amount: int):
        self.money -= amount
        other.money += amount

    @property
    def am_i_rich(self) -> bool:
        return self.money > 200

    @property
    def age(self) -> int:
        now = dt.datetime.now()
        return (now - self.birthday).days // 365

    def __del__(self):

        print(f'del {self}')


myself = Person(first_name='Alex', surname='Bush')

my_name = myself.name
my_json_data = myself.__dict__
myself.money = 1521
my_json_data2 = myself.__dict__

myself.beg_money(300).beg_money(20).beg_money(60)
#       myself       |
#                    | myself      |


you = Person(first_name='Bob', surname='Trump')
del you

# myself.lend_money(you, 500)
# myself.lend_money(you, 1)

print(555555555555555555555555)

myself.age

pass

# def foo(n):
#     pass
#
# foo.something = 5656565
#
# foo_data = foo.__dict__
