"""
Подвиг 6. В функцию get_data() передается параметр value:

def get_data(value):
    match value:
        # здесь продолжайте программу

    return None

Необходимо дописать оператор match/case в этой функции так, чтобы для каждого типа данных (int, float и str) формировалась
переменная со значением value и возвращалась функцией (непосредственно из блока case).

P. S. Вызывать функцию не нужно, только дописать.
"""


def get_data(value):
    match value:
        case int() | float() | str() as typed_value:
            return typed_value

    return None
