def get_add(a, b):
    type_a = type(a)
    type_b = type(b)
    if type_a == type_b and type_a == str:
        return a + b
    elif type_a in (int, float) and type_b in (int, float):
        return a + b
    return None

print(get_add(2, 3))
print(get_add('a', 'b'))
print(get_add(2, 3.2))
