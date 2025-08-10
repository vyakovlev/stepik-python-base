"""
Подвиг 5.
На вход программе подается строка с email-адресами, записанных через пробел.
Нужно прочитать эту строку и среди email-адресов оставить только корректно записанные адреса.
Полагается, что к таким относятся те, что используют только латинские буквы, цифры и символ подчеркивания.
Также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел в порядке их следования в исходной строке.
"""

import string

src_emails = input().split()


def is_valid_email(e: str) -> bool:
    (part1, part2) = e.split('@')
    for i in part1:
        if i not in (string.ascii_letters + string.digits + '_'):
            return False
    has_dot = False
    for i in part2:
        if i not in (string.ascii_letters + string.digits + '_' + '.'):
            return False
        if i == '.':
            has_dot = True
    return True if has_dot else False


emails = filter(is_valid_email, src_emails)
print(*emails)
