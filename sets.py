my_set = set()
my_set_2 = {2, 66, 100, 88, 999, 88}

# YOU
cities = ['NY', 'San Francisco', 'Atlanta', 'NY']
print('Lviv' in cities)

visited_cities_by_yura = set(cities)

# add element
visited_cities_by_yura.add('Odesa')

# delete element
visited_cities_by_yura.remove('NY')
# visited_cities.remove('Lviv')
visited_cities_by_yura.discard('Lviv')  # no error

# check element in set
print('Lviv' in visited_cities_by_yura)

# I
my_cities = {'NY', 'San Francisco', 'NY', 'Vinnytsa'}

# union
all_cities = my_cities | visited_cities_by_yura

# common elements
common_cities = my_cities & visited_cities_by_yura

# only presented in visited cities
only_presented_in_visited_cities = visited_cities_by_yura - my_cities

# to visit (симетрична різниця) symmetric_difference
to_visit = visited_cities_by_yura ^ my_cities

# iteration
for city in to_visit:
    print(f'Buying ticket to {city}')


dict_to_set = set(
    {'b': 55, 'm': 80}
)

string_to_set = set('1111111111122222222222333333333dddddddddd dd' * 500)

pass