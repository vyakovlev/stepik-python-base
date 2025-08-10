"""
Подвиг 3. Объявите в программе функцию с именем get_biggest_city, которой можно передавать произвольное количество
названий городов (строк) через аргументы. Например:

get_biggest_city('Город 1', 'Город 2', 'Город 3', 'Город 4')
Данная функция должна возвращать название города (строку) наибольшей длины. Если таких городов несколько, то первый
переданный (из наибольших). Программу реализовать без использования сортировки.

P.S. Функцию выполнять не нужно, только определить.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.3

Sample Input:

Питер Москва Самара Воронеж
Sample Output:

Воронеж

"""


def get_biggest_city(*args):
    ind = 0
    max_len = 0
    for i, c in enumerate(args):
        if len(c) > max_len:
            ind = i
            max_len = len(c)
    return args[ind]


cities = input().split()
print(get_biggest_city(*cities))

