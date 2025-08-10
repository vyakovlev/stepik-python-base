a = 3
# a = int(input())
gen1 = [abs(x) for x in range(-a, a + 1)]
gen2 = [x ** 3 for x in gen1]
c = 1
for i in gen2:
    print(i, end=' ')
    if c == 4:
        break
    c += 1
