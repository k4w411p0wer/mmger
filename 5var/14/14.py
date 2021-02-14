a = 9**1700 + 3**1800 - 3**350 + 2
n = 0
while a:
    if a % 3 == 2:
        n += 1
    a //= 3
print(n)
