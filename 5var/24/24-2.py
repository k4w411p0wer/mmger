with open('24.txt') as file:
    text = file.read()
longest_strings = {chr(i): 0 for i in range(ord('k'), ord('p') + 1)}
start = text[0]
n = 0
for i in range(1, len(text) - 1):
    if text[i + 1] == text[i]:
        n += 1
        continue
    if text[i + 1] == start:
        longest_strings[text[i]] = max(n + 1, longest_strings[text[i]])
    n = 0
    start = text[i]
print(max(longest_strings.values()))
