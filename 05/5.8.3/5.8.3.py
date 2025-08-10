"""
Подвиг 3. На вход программе подается натуральное число N. Прочитайте его и с помощью list comprehension сформируйте
двумерный список размером N x N, состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это
элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). Полученный двумерный
список отобразите в виде таблицы чисел, как показано в примере ниже.
"""

# N = 4
# lst = [[0] * N for i in range(N)]
# for i in range(N):
#     for j in range(N):
#         lst[i][j] = 1 if j == i else 0

# lst = [
#     t[i].append(1 if j == i else 0) for j in range(N)
#     t[i] for i in range(N) t[j].append(1 if j == i else 0)
# ]

# lst = [
#     [row[i] = 1 for n in row]
#     for i, row in enumerate(lst)
# ]

N = int(input())
lst = [
    [
        1 if j == i else 0 for j in range(N)
    ]
    for i in range(N)
]

for r in lst:
    print(*r)
