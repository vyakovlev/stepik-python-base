n = int(input())
a = 0
b = 1
c = 1
i = 0
while i < n:
    print(c, end=' ')
    c = a + b
    a, b = b, c
    i += 1
