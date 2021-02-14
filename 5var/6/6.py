def f(n):
    s = 1
    while n <= 210:
        s *= 3
        n += 30
    return s


i = 0
while f(i) != 729:
    i += 1
else:
    print(i)
