"""
Подвиг 3. Имеется программа (см. листинг ниже), где читается глобальная переменная WIDTH (из входного потока) и функция
с именем func1. Допишите в теле функции команду, которая бы позволяла изменять глобальную переменную WIDTH.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.9.3

Sample Input:

12
Sample Output:

13

"""

WIDTH = int(input())


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())
