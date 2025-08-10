"""
Подвиг 2. Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет,
можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина любой его стороны
должна быть меньше суммы двух других). Если  проверка проходит, функция должна возвращать булево значение True, а
иначе False.

Вызывать функцию не нужно, только объявить.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.2.2

Sample Input:

3 4 5
Sample Output:

True


"""


def is_triangle(a, b, c):
    ranges = sorted([a, b, c])
    return True if ranges[0] + ranges[1] > ranges[2] else False


print(is_triangle(3, 4, 5))
