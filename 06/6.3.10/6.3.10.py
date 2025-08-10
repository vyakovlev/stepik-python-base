"""
Подвиг 10. На вход программе подаются строки (пункты меню), каждая с новой строки, в формате:

название_1 URL-адрес_1
название_2 URL-адрес_2
...
название_N URL-адрес_N

В программе уже реализовано чтение этих строк и сохранение их в списке:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо преобразовать список lst_in так, чтобы получился кортеж menu следующего вида:

((название_1, URL-адрес_1), (название_2, URL-адрес_2), ... (название_N, URL-адрес_N))

Полученный кортеж вывести на экран командой:

print(menu)
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.3.10

Sample Input:

Главная home
Python learn-python
Java learn-java
PHP learn-php
Sample Output:

(('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))

"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
menu = tuple(
    tuple(line.split()) for line in lst_in
)

print(menu)

