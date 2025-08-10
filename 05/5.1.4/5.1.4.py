n = int(input())
s = 0
i = 1

while i <= n:
    s += 1/i
    i += 1

print(f"{s:.3f}")