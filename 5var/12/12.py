a = '7' * 112
while '111' in a or '7777' in a:
    if '111' in a:
        a = a.replace('111', '7', 1)
    else:
        a = a.replace('7777', '1', 1)
print(a)
