import utils


def main():
    dealership1_cars_number = 10
    dealership2_cars_number = 30

    print(utils.has_permission_drive_car(1980))
    print(utils.has_permission_drive_car(1990))
    print(utils.has_permission_drive_car(2007))

    strings = utils.create_joined_string(data_list=[55555555555, 'kjjbh'], divider=', ')
    strings = utils.create_joined_string(divider='==', data_list=['list 2', 'kjjbh', 5555555, 666666])
    strings = utils.create_joined_string(['list 2', 'kjjbh', 5555555, 666666], divider='=+=', )
    strings = utils.create_joined_string(['list 2', 'kjjbh', 5555555, 666666])

    print(strings)


    # site_data
    total_cars = utils.get_cars_in_our_dealerships(dealership1_cars_number, dealership2_cars_number)
    print(total_cars)


    # mobile-app
    cars_number_from_mobile = [111, 5256]
    total_cars_mobile = utils.get_cars_in_our_dealerships(cars_number_from_mobile[0], cars_number_from_mobile[1])
    print(total_cars_mobile)


    print(1111, 2222, 3333333, sep='+++', end='0')
    print(4444, 5555, 6666666, sep='===')
    print(77777, 5555, 6666666)

    print(utils.get_multiplied_string('a'))
    print(utils.get_multiplied_string('b'))
    print(utils.get_multiplied_string('c'))
    print(utils.get_multiplied_string('d'))
    print(utils.get_multiplied_string('e'))
    print(utils.get_multiplied_string('f'))
    print(utils.get_multiplied_string('g'))
    print(utils.get_multiplied_string('h', 3))
    print(utils.get_multiplied_string('j', multiplicator=12))


main()
