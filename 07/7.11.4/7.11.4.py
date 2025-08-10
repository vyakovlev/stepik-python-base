"""
Подвиг 4. На вход программе поступают две строки. В каждой строке записаны слова через пробел. Прочитайте эти строки и
сохраните их в двух переменных.

Объявите функцию с двумя параметрами, которой передаются строки со словами и преобразовываются в два списка из слов.
Функция должна возвращать кортеж с этими списками в порядке: сначала первый список (первой строки), затем - второй.

Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из
первого списка, а значениями - соответствующие элементы из второго списка. Длины списков полагаются равными. Полученный
словарь должен возвращаться при вызове декоратора.

Примените декоратор к первой функции и вызовите ее для прочитанных строк. Результат (словарь d) отобразите на экране
командой:

print(*sorted(d.items()))
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.11.4

Sample Input:

house river tree car
дом река дерево машина
Sample Output:

('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

"""

words1, words2 = input(), input()


def make_words_dict(func):
    def wrapper(*args, **kwargs):
        # lst1, lst2 = func(*args, *kwargs)
        # wd = dict(zip(*func(*args, **kwargs)))
        lst1, lst2 = func(*args, *kwargs)
        wd = {
            lst1[i]: lst2[i]
            for i in range(len(lst1))
        }

        # wd = {}
        # for i, val in enumerate(lst1):
        #     wd[val] = lst2[i]
        # wd = dict(func(*args, *kwargs))
        return wd

    return wrapper


@make_words_dict
def get_words(w1: str, w2: str):
    return tuple([w1.split(), w2.split()])


d = get_words(words1, words2)
print(*sorted(d.items()))
