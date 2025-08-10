"""
Подвиг 4. Объявите в программе функцию с именем get_data_fig для вычисления периметра произвольного N-угольника. На
 вход этой функции передаются N длин сторон через ее аргументы. Дополнительно могут быть указаны именованные аргументы:

tp - булево значение True/False;
color - целое числовое значение;
closed - булево значение True/False;
width - целое значение.
Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в порядке
 их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует, его возвращать не
 нужно (пропустить).

P.S. Функцию выполнять не нужно, только объявить.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.5.4

Sample Input:

1 2 3 4 3 2 4
Sample Output:

19
19 True
19 True 7
19 False 2.0

"""


# def get_data_fig(*args, tp=None, color=None, close=None, width=None):
def get_data_fig(*args, **kwargs):
    s = sum(args)
    opt_args = ["tp", "color", "closed", "width"]
    extra_args = [str(kwargs[k]) for k in opt_args if k in kwargs]
    return (s, ) + tuple(extra_args)


# N = list(map(int, input().split()))
N = list(map(int, "1 2 3 4 3 2 4".split()))
print(get_data_fig(*N))
print(get_data_fig(*N, tp=True))
