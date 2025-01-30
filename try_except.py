import logging

cities = ['Atlanta', 'NY1', 'San Francisco', 'Atlanta', 'NY']
visited_cities_by_yura = set(cities)
# visited_cities_by_yura.remove('Lviv')


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

divider = 1
if divider == 0:
    defined_city = 'Odesa'
else:
    division = int(4 / divider)
    len_cities = len(cities)
    if len_cities >= division - 1:
        defined_city = cities[division]
        if defined_city == 'Atlanta':
            raise ValueError('I cannot go to Atlanta. Poor duck (((')
    else:
        logging.debug('We have got IndexError')
        raise IndexError

try:
    division = int(455555555555 / divider)
    defined_city = cities[division]
    if defined_city == 'Atlanta':
        raise ValueError('I cannot go to Atlanta. Poor duck (((')
except ZeroDivisionError:
    defined_city = 'Odesa'
except IndexError:
    logging.debug('We have got IndexError')
    raise
else:
    logging.debug('We have no issues')
finally:
    logging.debug('We have ran finally bloc')
    # defined_city = 'Kyiv'

print(defined_city)
