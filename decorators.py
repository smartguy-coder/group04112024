# print
#
# some = print
#
# print(id(print))
# print(print)
# print(id(some))
# print(some)
#
# some(55556666)
from typing import Callable


def foo(gas: int) -> str:
    return f'foo///{gas}'

def foo2(gas: int, electropower: int) -> str:
    return f'foo222///{gas} {electropower}'

# n = foo()
# print(                  type(foo)                )
#
# print(foo.__code__)
# print(foo.__annotations__)
#
# foo.data = 50
# foo.another = 150
# print(foo.__dict__)
#
# print(n)

# some = foo
# #
# m = some(      55       )
# print(m)


def call_callable_function(func: Callable, *args, **kwargs) -> None:
    res = func(*args, **kwargs)
    if '222' in res:
        print(222, 'found')
    return


# call_callable_function(foo, 20)
# call_callable_function(foo, gas=222)
# call_callable_function(foo2, gas=10, electropower=20)

# def math(a, b):
#     return a + b
#
#
# res = math(5, 8)
#
# print(res)
#
# res = math(55, 8)
#
# print(res)
