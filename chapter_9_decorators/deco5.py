"""
Реализовать ф-цию counter (вебинар А.Беренда)
"""
from typing import Callable


def make_counter() -> Callable[[], int]:
    cnt = 0

    def counter() -> int:
        nonlocal cnt
        cnt += 1
        return cnt
    return counter


counter1 = make_counter()
counter2 = make_counter()

print(counter1(), counter2())
print(counter2(), counter2())
print(counter1(), counter1())
print(counter1(), counter2())
