import utils


def test_is_even_positive():
    number = 6
    expected_result = True
    actual_result = utils.is_even(number)
    assert actual_result == expected_result


def test_is_even_negative():
    number = 5
    expected_result = False
    actual_result = utils.is_even(number)
    assert actual_result == expected_result


def test_get_of_strings():
    items = []
    expected_result = []
    actual_result = utils.get_list_of_strings(items)
    assert actual_result == expected_result


def test_get_of_strings_not_empty():
    items = [22, 'apple']
    expected_result = ['apple']
    actual_result = utils.get_list_of_strings(items)
    assert actual_result == expected_result


def test_is_multiply_number():
    number = 5
    expected_result = 50
    actual_result = utils.multiply_ten(number)
    assert actual_result == expected_result


def test_is_multiply_number_negative():
    number = -2.5
    expected_result = 25
    actual_result = utils.multiply_ten(number)
    assert actual_result == expected_result


def test_filter_strings_with_n():
    list_strings = []
    expected_result = []
    actual_result = utils.filter_strings_with_n(list_strings)
    assert actual_result == expected_result


def test_filter_strings_with_n_result():
    list_strings = ['n', 'N', 'apple']
    expected_result = ['n', 'N']
    actual_result = utils.filter_strings_with_n(list_strings)
    assert actual_result == expected_result
