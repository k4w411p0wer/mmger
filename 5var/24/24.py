import re


longest_strings = {chr(i): 0 for i in range(ord('k'), ord('p') + 1)}
with open('24.txt') as file:
    text = file.read()[:-1]

c = set(chr(i) for i in range(ord('k'), ord('p') + 1))
for i in c:
    m = c.copy()
    m.remove(i)
    for j in m:
        v = re.findall(r'{0}{1}+{0}'.format(j, i), text)
        if v:
            longest_strings[i] = max(
                max(len(i) - 2 for i in v),
                longest_strings[i]
            )
print(max(longest_strings.values()))
