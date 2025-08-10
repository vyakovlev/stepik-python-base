"""
Подвиг 3. Объявите функцию с именем is_large, которая принимает строку (в качестве параметра) и возвращает булево
значение False, если длина строки меньше трех символов, иначе True.

Вызывать функцию не нужно, только объявить.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.2.3

Sample Input:

Я люблю Python!
Sample Output:

True

"""


def is_large(s):
    return False if len(s) < 3 else True


print(is_large("Я люблю Python!"))
