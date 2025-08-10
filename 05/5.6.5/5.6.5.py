"""
Подвиг 5. На вход программе подается двумерный список размерностью 5 х 5 элементов, состоящий из целых чисел (пример
см. ниже). В программе уже реализовано их чтение и сохранение в списке:

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
Необходимо проверить, является ли этот двумерный список симметричным относительно главной диагонали.
Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний. Выведите на экран
"ДА", если матрица (таблица чисел) симметрична и "НЕТ" в противном случае.
"""

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# raw_input = """
# 7 3 4 5 1
# 3 7 7 8 9
# 4 7 7 0 3
# 5 8 0 7 1
# 6 9 4 1 7
# """
# raw_lines = raw_input.split('\n')
# lst_in = [list(map(int, x.strip().split())) for x in raw_lines[1:-1]]


def get_vertical(c_i):
    column = []
    for r_i in range(len(lst_in)):
        column.append(lst_in[r_i][c_i])

    return column


def get_horizontal(r_i):
    return lst_in[r_i]


sym = False
for i in range(len(lst_in)):
    c = get_vertical(i)
    r = get_horizontal(i)
    if c != r:
        break
else:
    sym = True

print(["НЕТ", "ДА"][sym])
