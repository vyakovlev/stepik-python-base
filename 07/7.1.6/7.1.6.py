"""
Подвиг 6. Объявите в программе функцию, которая в качестве параметра принимает список (list), находит максимальное,
минимальное и сумму значений этого списка и выводит результат на экран в виде строки (без кавычек):

"Min = v_min, max = v_max, sum = v_sum"

где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.

После объявления функции прочитайте (с помощью функции input) список целых чисел, записанных в одну строку через
пробел, и вызовите функцию с передачей ей этого списка.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.1.6

Sample Input:

8 11 5 -10 12 0
Sample Output:

Min = -10, max = 12, sum = 26

"""


def calc_values(lst):
    v_min = min(lst)
    v_max = max(lst)
    v_sum = sum(lst)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")


my_lst = list(map(int, input().split()))
calc_values(my_lst)
