"""
Значимый подвиг 6. (Для закрепления предыдущего материала). Объявите в программе функцию с именем str_min, которая
сравнивает две переданные строки (через два первых параметра) и возвращает минимальную из них (то есть, выполняется
лексикографическое сравнение строк). Следом объявите еще две аналогичные функции:

с именем str_min3 для поиска минимальной строки из трех переданных строк;
с именем str_min4 для поиска минимальной строки из четырех переданных строк.
Причем при реализации функций str_min3 и str_min4 следует использовать вызов (результат работы) функции str_min.

P.S. Выполнять функции не нужно, только объявить.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.6


"""


def str_min(a, b):
    return a if a < b else b


def str_min3(a, b, c):
    s1 = str_min(a, b)
    s2 = str_min(b, c)
    return s1 if s1 < s2 else s2


def str_min4(a, b, c, d):
    s1 = str_min3(a, b, c)
    s2 = str_min3(b, c, d)
    return s1 if s1 < s2 else s2


# strs = [input().split() for _ in range(3)]
# print(str_min(strs[0][0], strs[0][1]))
# print(str_min3(strs[1][0], strs[1][1], strs[1][2]))
# print(str_min4(strs[2][0], strs[2][1], strs[2][2], strs[2][3]))
#
#
