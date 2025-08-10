"""
Подвиг 3. На вход программе подается натуральное число N (N > 8). Необходимо его прочитать и объявить функцию-генератор, которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков. Значение N передается в функцию-генератор первым аргументом. Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз.

Сгенерируйте с помощью функции-генератора первые пять паролей и выведите их в столбик (каждый с новой строки).

Подсказка: сгенерировать случайный индекс indx в диапазоне [a; b] для выбора символа из chars можно с помощью функции randint модуля random:

import random
random.seed(1)
indx = random.randint(a, b)

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.2.3

Sample Input:

10

Sample Output:

riGp?58WAm
!dX3a5IDnO
dcdbWB2d*C
4?DSDC6Lc1
mxLpQ@2@yM
"""

from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)

N = int(input())
# N = 10
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

def get_pass(pass_len):
    while True:
        gen_pass = []
        for i in range(pass_len):
            gen_pass.append(chars[random.randint(0, len(chars) - 1)])
        yield ''.join(gen_pass)


pass_gen = get_pass(N)
for i in range(5):
    print(next(get_pass(N)))
