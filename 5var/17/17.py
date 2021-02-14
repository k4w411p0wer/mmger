min_ = float('inf')
max_ = n = 0
for i in range(5835 + 1, 9762 + 1, 3):
    if i % 7 == 2 and (i % 8 == 5 or i % 11 == 5):
        if min_ > i:
            min_ = i
        if max_ < i:
            max_ = i
        n += 1
print(n, max_ - min_)
