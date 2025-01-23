from typing import Callable



def master(func: Callable) -> Callable:

    def subordinate(*args, **kwargs):
        # -----------------------------------------
        # before execution
        print(args)
        print(kwargs)
        see_scratches = input('Do you see scratches (yes/no)> ')
        if see_scratches == 'yes':
            print('I do not want to pay for this. Call manager')
            return
        # -----------------------------------------


        result = func(*args, **kwargs)  # must be here!!!!!!!!!!!!!!!


        # -----------------------------------------
        # after execution
        print('No scratches was seen')
        if '5' in result:
            print('5 found')
        # -----------------------------------------

        return result

    return subordinate  # no round brackets !!!!!!!!!!!!!!


@master
def foo(gas: int) -> str:
    # see_scratches = input('Do you see scratches (y/n)> ')
    # if see_scratches == 'y':
    #     print('I do not want to pay for this. Call manager')
    #     return

    return f'foo///{gas}'


@master
def foo2(gas: int) -> str:
    # see_scratches = input('Do you see scratches (y/n)> ')
    # if see_scratches == 'y':
    #     print('I do not want to pay for this. Call manager')
    #     return

    return f'foo222///{gas}'


# foo = master(foo)
# foo2 = master(foo2)


res = foo(5)
print(res)

res = foo2(22)
print(res)
