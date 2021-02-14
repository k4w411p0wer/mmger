def solution1():
    a = []
    for n in range(1150 + 1):
        if n < 20:
            a.append(2)
        elif n < 150:
            a.append(1 + 2 * a[n - 17])
        elif n < 1000:
            a.append(-3 + a[n - 23])
        else:
            a.append(2 + a[n - 42])
    print(a[1150])


def solution2():
    def f(n):
        if n < 20:
            return 2
        if n < 150:
            return 1 + 2 * f(n - 17)
        if n < 1000:
            return -3 + f(n - 23)
        return 2 + f(n - 42)

    print(f(1150))


solution1()
solution2()
