# name = input('Введіть своє ім`я: ') + '\n\n          \t' + '\n\n          \t'
name = input('Введіть своє ім`я: ')
# age = input('Введіть свій вік: ')


# name = name.title()
# name = name.strip()
# name = name.strip('0123456789 j')
# name = name.lstrip('0123456789 j')
# name = name.rstrip('0123456789 j')
# name = name.lower()
# name = name.upper()

name.replace('0', '1')

# name = name.title().strip('0123456789 ')
# name = name.replace('  ', ' ', 2)
name = name.replace('           ', ' ').replace('  ', ' ')
name = name.capitalize()

multiplication = '*-*~' * 50

print(multiplication)

# german = 'ẞ'
# german = 'ß'
# german = german.lower()
# german = german.upper()

# print(german)

print(name)
