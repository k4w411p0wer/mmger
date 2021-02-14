import bisect
from itertools import groupby

with open('26-1.txt') as file:
    receipts = []
    n, m = map(int, file.readline().split())
    for line in file:
        bisect.insort(receipts, int(line))

m_receipts = receipts[-m:]
s1 = sum(m_receipts)
s2_receipts = []
l = []
for _, elements in groupby(m_receipts):
    a = list(elements)
    if len(a) > 1:
        s2_receipts.extend(a[:-1])
    l.append(a.pop())

while sum(s2_receipts) <= 0.9 * s1:
    s2_receipts.append(l.pop())

s2 = sum(s2_receipts)

print(s1, s2)
