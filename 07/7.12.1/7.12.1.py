"""
Подвиг 1. На вход программе подаются целые числа, записанные через пробел. Прочитайте эту строку и сохраните через
 какую-либо переменную.

Напишите функцию, которая имеет один параметр, преобразовывает переданную ей строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для прочитанной строки. Результат
(сумму) отобразите на экране.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.12.1

Sample Input:

5 6 3 6 -4 6 -1
Sample Output:

26

"""

from functools import wraps


def decor_get_sum(start: int):
    def get_decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res + start

        return wrapper

    return get_decor


@decor_get_sum(5)
def get_sum(n: str):
    return sum([int(x) for x in n.split()])


nums = input()
# nums = "5 6 3 6 -4 6 -1"

print(get_sum(nums))
