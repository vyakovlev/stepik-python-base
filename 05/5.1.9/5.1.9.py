n = int(input())
c = 1

i = 1
while i <= n:
    if i % 3 == 0:
        c *= 2
    i += 1

print(c)