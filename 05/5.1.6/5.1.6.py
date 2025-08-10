# s = "osnovnye--metody-----slovarey"
s = input()
s_lst = list(s)
i = 0

while i < len(s_lst):
    if s_lst[i] == '-':
        i += 1
        while s_lst[i] == '-':
            del s_lst[i]
    else:
        i += 1

print(*s_lst, sep='')
