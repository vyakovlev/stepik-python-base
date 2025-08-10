"""
Значимый подвиг 4. Имеется таблица с данными, представленная в формате:

Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
...
N;Балакирев;4;Да

Данные этого списка необходимо разбить по разделителю ";" и представить в виде двумерного (вложенного) кортежа в формате:

( ('Номер', 'Имя', 'Оценка', 'Зачет'), (1, 'Иванов', 3, 'Да'), (2, 'Петров', 2, 'Нет'), ... )

При этом все числа должны быть представлены как целые числа. Затем, отсортировать этот кортеж так, чтобы столбцы шли в порядке:

Имя;Зачет;Оценка;Номер

Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и присвоен переменной с именем t_sorted.

Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
"""

import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
    "Номер;Имя;Оценка;Зачет",
    "1;Портос;5;Да",
    "2;Арамис;3;Да",
    "3;Атос;4;Да",
    "4;д'Артаньян;2;Нет",
    "5;Балакирев;1;Нет",
]

# здесь продолжайте программу (используйте список строк lst_in)
# scores = []
# for s in lst_in:
#     items = s.split(';')
#     if items[0] != "Номер":
#         items[0] = int(items[0])
#         items[2] = int(items[2])
#     scores.append(tuple(items))

# scores = tuple(scores)

# def sort_by_name(s_i: tuple) -> bool:
#     return 0 if s_i[1] == 'Имя' else s_i[0]


# scores_sorted = sorted(scores, key=sort_by_name)
# t_sorted = tuple(
#     tuple(
#         [sc[1], sc[3], sc[2], sc[0]]
#      ) for sc in scores_sorted
# )


# header = ("Имя;Зачет;Оценка;Номер".split(';'))
scores = tuple(
    tuple(int(f) if f.isdigit() else f for f in l.split(';')) for l in lst_in
)


def sort_by_id(score: tuple) -> bool:
    return score[0] if isinstance(score[0], int) else -1


scores_sorted = sorted(scores, key=sort_by_id)
t_sorted = tuple(
    tuple(
        [sc[1], sc[3], sc[2], sc[0]]
     ) for sc in scores_sorted
)
print()
