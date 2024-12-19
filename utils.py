def is_even(number: int | float) -> bool:
    print(number)
    print(number % 2)
    _is_even = number % 2 == 0
    return _is_even


def get_list_of_strings(items: list) -> list[str]:
    result = []
    for item in items:
        if type(item) == str:
            result.append(item)
    return result


def multiply_ten(number: int | float) -> int | float:
    result = number * 10
    result = abs(result)
    return result


def filter_strings_with_n(strings: list[str]) -> list[str]:
    result = []
    for string in strings:
        if 'n' in string or 'N' in string:
            result.append(string)
    return result
