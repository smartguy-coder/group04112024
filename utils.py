import constants


def get_cars_in_our_dealerships(dealership1_cars: int, dealership2_cars: int) -> int:
    total_cars = dealership1_cars + dealership2_cars
    return total_cars


def create_joined_string(data_list: list, divider: str = ', ') -> str:
    result = divider.join(map(str, data_list))
    return result


def get_multiplied_string(letter: str, multiplicator: int = 5) -> str:
    result = letter * multiplicator
    return result


def get_list_with_numbers() -> list[int | float]:
    result = [11235, 23.65]
    return result


def has_permission_drive_car(birth_year: int) -> bool:
    """
    according to the law #5656 check if person has permission to drive a car
    https://zakon.rada.gov.ua/laws/show/1306-2001-п#Text
    """
    age = constants.CURRENT_YEAR - birth_year
    has_permission = age >= constants.MIN_DRIVE_AGE
    return has_permission


def send_sms(recipient: str, message: str) -> None:
    print(f'Send sms to {recipient} with {message=}')


def send_email(recipient: str, message: str) -> None:
    raise NotImplementedError
