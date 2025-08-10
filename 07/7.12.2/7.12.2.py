"""
Подвиг 2. Объявите функцию, которая переводит символы строки в нижний регистр (малые буквы) и возвращает результат.
Определите декоратор для этой функции, который имеет один параметр tag, определяющий строку с названием тега и
начальным значением "h1". Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.

Пример заключения строки "python" в тег h1:

<h1>python</h1>

Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для строки s, прочитанной из
входного потока:

s = input()
Результат работы декорированной функции отобразите на экране.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.12.2

Sample Input:

Декораторы - это классно!
Sample Output:

<div>декораторы - это классно!</div>

"""

from functools import wraps


def tag_decorator(tag: str = 'h1'):
    def lower_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f"<{tag}>{res}</{tag}>"

        return wrapper

    return lower_decorator


@tag_decorator(tag='div')
def to_lower(string: str):
    return string.lower()


s = input()
print(to_lower(s))
