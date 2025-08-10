"""
Значимый подвиг 7.
В программе инициализируется двумерное игровое поле размером N x N (N - натуральное число читается из входного потока), представленное в виде вложенного списка:

P = [[0] * N for i in range(N)]

Требуется расставить на поле P случайным образом M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг с другом (то есть, вокруг каждой
единицы должны быть нули, либо граница поля).
P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.
"""

import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
# N = int(input())
N = 7
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
M = 10

def get_point_value(y: int, x: int) -> int:
    if y < 0 or y > N - 1 or x < 0 or x > N - 1:
        return 0
    try:
        return P[y][x]
    except IndexError:
        return 0


def put_point():
    test_point_y = random.randint(0, N - 1)
    test_point_x = random.randint(0, N - 1)
    close_points = (
        (test_point_y - 1, test_point_x - 1),
        (test_point_y - 1, test_point_x),
        (test_point_y - 1, test_point_x + 1),
        (test_point_y + 1, test_point_x - 1),
        (test_point_y + 1, test_point_x),
        (test_point_y + 1, test_point_x + 1),
        (test_point_y, test_point_x - 1),
        (test_point_y, test_point_x + 1)
    )
    close_points_value = sum(get_point_value(y, x) for y, x in close_points)
    # print(f"x={test_point_x}, y={test_point_y}, close={close_points_value}")
    if close_points_value < 1:
        P[test_point_y][test_point_x] = 1
        return True
    else:
        return False


set_points = 0
while set_points <= M:
    if put_point():
        set_points += 1

print()
