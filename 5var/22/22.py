def f(x):
    k, r, y = 0, 9, x % 10
    while x:
        k += 1
        if r > x % 10:
            r = x % 10
        x //= 10
    r = y - r
    return k, r


i = 0
while f(i) != (4, 3):
    i += 1
else:
    print(i)
