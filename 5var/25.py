for i in range(3954, 8979 + 1):
    dividers = set()
    for j in range(1, int(i**0.5) + 1):
        if not i % j:
            dividers.update((j, i//j))
    if 41 <= len(dividers) <= 45:
        print(i, len(dividers))
