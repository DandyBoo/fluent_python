"""
Данный пример взят из ТГ канала "Душно и точка".
"""
import functools


def decorator_1(func):
    print('d1')

    @functools.wraps(func)
    def _wraps(*args, **kwargs):
        print('ed1')
        return func(*args, **kwargs)
    return _wraps


def decorator_2(func):
    print('d2')

    @functools.wraps(func)
    def _wraps(*args, **kwargs):
        print('ed2')
        return func(*args, **kwargs)

    return _wraps


@decorator_1
@decorator_2
def add(a, b):
    return a + b


print("O_o")
print(add(3, 5))

# add = decorator_1(decorator_2(add))
