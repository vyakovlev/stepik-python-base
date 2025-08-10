"""
Подвиг 8. Объявите в программе функцию с одним параметром, которая проверяет корректность переданного ей email-адреса
в виде строки. Полагается, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы
могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит "ДА", иначе "НЕТ".

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим
аргументом.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.1.8

Sample Input:

sc_lib@list.ru
Sample Output:

ДА

"""


def print_valid_email(email):
    email_list = list(email)
    is_valid = True
    if '@' not in email_list:
        is_valid = False
    else:
        email_list.remove('@')
    if '.' not in email_list:
        is_valid = False
    else:
        email_list.remove('.')
    for letter in email_list:
        if not ('a' <= letter <= 'z' or 'A' <= letter <= 'Z' or '0' <= letter <= '9' or letter == '_'):
            is_valid = False
            break

    print("ДА" if is_valid else "НЕТ")


my_email = input()
# my_email = "sc_lib@list.ru"
print_valid_email(my_email)
