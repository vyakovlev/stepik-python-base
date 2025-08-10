"""
Подвиг 4. На вход программе подается двумерный список размерностью 5 х 5 элементов, состоящий из нулей и в некоторых
позициях единицы (см. пример ниже). В программе уже реализовано их чтение и сохранение в списке:

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали. То есть, вокруг каждой
единицы должны быть нули. Если проверка проходит вывести на экран "ДА", иначе "НЕТ".
"""

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]


def get_elem(i1, j1):
    elem = 0
    if 0 <= i1 <= 4 and 0 <= j1 <= 4:
        elem = lst_in[i1][j1]
    return elem


def sum_borders(i1, j1):
    elems = [
        get_elem(i1, j1 - 1),
        get_elem(i1, j1 + 1),
        get_elem(i1 - 1, j1),
        get_elem(i1 + 1, j1),
        get_elem(i1 - 1, j1 - 1),
        get_elem(i1 + 1, j1 - 1),
        get_elem(i1 - 1, j1 + 1),
        get_elem(i1 + 1, j1 + 1),
    ]
    return sum(elems)


contact = False
for i in range(0, 5):
    for j in range(0, 5):
        item = lst_in[i][j]
        if item == 0:
            continue
        sum_brds = sum_borders(i, j)
        if sum_brds > 0:
            contact = True
            break
    if contact:
        break

print(["ДА", "НЕТ"][contact])



# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# # здесь продолжайте программу (используйте список lst_in)
# n = len(lst_in) - 1
#
# for i in range(n):
#     for j in range(n):
#         if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] + lst_in[i][j + 1] > 1:
#             print('НЕТ')
#             break
#     else:
#         continue
#     break # выход из внешнего цикца
# else:
#     print('ДА')