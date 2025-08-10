"""
Подвиг 3. Объявите в программе функцию с именем check_password, которая первым параметром принимает строку (пароль) и
имеет второй формальный параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять, есть ли
в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов. Если проверка проходит, то функция
возвращает булево True, иначе False.

P. S. Вызывать функцию не нужно, только объявить.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.4.3

Sample Input:

12345678!
Sample Output:

True

"""


def check_password(passwd, chars="$%!?@#"):
    if len(passwd) < 8:
        return False

    return True if any(let in chars for let in passwd) else False


print(check_password(input()))

