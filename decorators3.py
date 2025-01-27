from datetime import datetime as dt
import os
from functools import wraps, cache
from cachetools import cached, LRUCache, TTLCache
import time


from typing import Callable


def log_work(filename: str = 'log_data.log') -> Callable:
    def log_work_inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # -----------------------------------------
            # before execution

            # -----------------------------------------

            result = func(*args, **kwargs)  # must be here!!!!!!!!!!!!!!!

            # -----------------------------------------
            # after execution
            current_time = dt.now()
            with open(filename, mode='a', encoding='utf-8') as file:
                file.write(f'{current_time};{func.__name__};{args};{kwargs};{result}\n')

            # -----------------------------------------

            return result

        return wrapper  # no round brackets !!!!!!!!!!!!!!

    return log_work_inner  # no round brackets !!!!!!!!!!!!!!


# log_work = log_work(foo)
@log_work('log_data.log')
@cache
def foo(number: int) -> int:
    # print(5555555555555555555555555555555555555555555555)
    return number + 22


@log_work()
@cached(cache=TTLCache(maxsize=5, ttl=2))
def foo2(data= 55) -> dict:
    """some docstring"""
    print('*' * 50)
    time.sleep(3)
    return {'data': data}


@log_work('log_data_other.log')
@log_work('log_data_other22.log')
def get_file_length(filename: str) -> int:
    size = os.path.getsize(filename)
    return size


foo(6)
foo(6)
foo(6)
foo(6)
foo(6)
foo(6)
foo(6)
foo(7)
foo(8)
foo2()
foo2(33)
foo2()
foo2()
foo2()
# foo2(33)
# foo2(44)
# foo2(18)
# foo2(33)
# foo2(55)
# foo2(556)
foo2()

get_file_length(filename='decorators3.py')
get_file_length('log_data.log')
pass
