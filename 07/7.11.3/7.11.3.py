"""
Подвиг 3. На вход программы поступает строка из целых чисел, записанных через пробел. Необходимо прочитать эту строку
и сохранить в какой-либо переменной.

Напишите функцию get_list с одним параметром, которая преобразовывает эту строку в список из целых чисел и возвращает
его. Определите декоратор для функции get_list, который сортирует список чисел по возрастанию. Результат сортировки
должен возвращаться в виде списка чисел при вызове декоратора.

Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:

print(*lst)
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.11.3

Sample Input:

8 11 -5 4 3 10
Sample Output:

-5 3 4 8 10 11

"""

nums = input()


def get_sorted(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sorted(res)

    return wrapper


@get_sorted
def get_list(n: str):
    return [int(x) for x in n.split()]


lst = get_list(nums)
print(*lst)

