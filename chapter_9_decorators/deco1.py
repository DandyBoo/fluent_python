"""
Когда Python выполняет декораторы.
Главное свойство декораторов – то, что они выполняются сразу после определения декорируемой функции.
Обычно на этапе импорта (т. е. когда Python загружает модуль).
Рассмотрим скрипт registration.py в примере 9.2.
"""

registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
