def foo(value=15):
    """some description"""
    return value + 2055


# anon = lambda value: value + 55
#
# print(anon(6))

my_functions = {
    'regular': foo,
    'lambda': lambda value=15: value + 55
}

func_name = input('enter your func name')
result_func = my_functions[func_name]
calculated_result = result_func(30)
pass