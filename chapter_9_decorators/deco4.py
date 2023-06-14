# Замыкания
"""Реализуем класс, объекты которого будут вести себя так:
avg(10) -> 10
avg(11) -> 10.5
avg(12) -> 11
"""


# class Averager:
#
#     def __init__(self):
#         self.storage = []
#
#     def __call__(self, value):
#         self.storage.append(value)
#         return sum(self.storage) / len(self.storage)
#
#
# avg = Averager()
#
# print(avg(10))
# print(avg(11))
# print(avg(12))


# реализация с помощью функции (неэффективный метод):
# def make_average():
#     storage = []
#
#     def get_avg(val):
#         storage.append(val)
#         return sum(storage) / len(storage)
#
#     return get_avg
#
#
# avg = make_average()
# print(avg(10))
# print(avg(11))
# print(avg(12))
# print(avg.__code__.co_freevars)


# реализация с помощью функции (эффективный метод):

def make_average():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))
