# classic decorator
import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something before")
        result = func(*args, **kwargs)
        print("Do something after")
        return result
    return wrapper


@decorator
def foo(a, b):
    """Сложение двух чисел."""
    return a+b


print(foo(2, 5))
# print(foo.__doc__, foo.__module__, foo.__qualname__)
