my_tuple = ('first', 'second', [])

print(my_tuple)
my_tuple[2].append(6666666666)
# my_tuple[2] = 5555555
tuple_to_list = list(my_tuple)

print(tuple_to_list)

list_to_tuple = tuple(tuple_to_list)

my_data = 55, 222
print(my_data)


def foo(first, second):
    print(f'{first=}, {second=}')


foo(56, 32)

# arguments = (1111, 333333)
# first, second = arguments
# pass


# arguments = (1111, 333333, 4444, 88888)
# first, second, *third = arguments
# pass


# arguments = (1111, 333333, 4444, 88888)
# first, *second, third = arguments
# pass


def foo2(*args, **kwargs):
    print(args)
    print(kwargs)
    pass


# foo2(gg={'data': 55}, another_one=7777777)


some_dict = {'name': 'Alex', 'age': 15}

# after items     some_dict.items()
# [('name', 'Alex'), ('age', 15)]


# for item in some_dict.items():
#     print(item)

for key, value in some_dict.items():
    print(key)
    print(value)
    print(6666666666666666666)
