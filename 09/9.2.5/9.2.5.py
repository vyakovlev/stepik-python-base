"""
Подвиг 5. Объявите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1). Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
"""


def gen_simple():
    dividers = [2]
    simple_one = 1
    while True:
        simple_one += 1
        if simple_one == 2:
            yield simple_one
        if simple_one % 2 == 0:
            continue
        for div in dividers:
            if simple_one % div == 0:
                break
        else:
            dividers.append(simple_one)
            # count += 1
            yield simple_one

simple_ones = gen_simple()
for i in range(20):
    print(next(simple_ones), end=' ')
