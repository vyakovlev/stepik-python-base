"""
Подвиг 4. Имеется следующий фрагмент программы с функцией parse_json и словарем json_data:

def parse_json(data):
    match data:
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения значения ключа
access с проверкой на тип bool и для выделения даты (первое значение списка) из поля data с проверкой, что data является списком.
Возвратите выделенные два значения в виде кортежа в формате (access, date).

P. S. В программе нужно только дописать шаблон. Вызывать функцию не нужно.
"""


def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': access, 'data': list([str(date), *_])} if type(access) is bool:
            return access, date
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
res = parse_json(json_data)
assert res[0] == False and res[1] == '26.05.2023'
