operations = (
    lambda n: n + 2,
    lambda n: 3 * n,
)
s1 = 35
limit = 808
positions = [[0] * (4 * limit) for j in range(4 * limit)]

for y in range(limit - 1, 0, -1):
    for x in range(limit - y - 1, 0, -1):
        variations = []
        for operator in operations:
            variations.append(positions[y][operator(x)])
            variations.append(positions[operator(y)][x])
        negative_positions = [i for i in variations if i <= 0]
        if negative_positions:
            positions[y][x] = -max(negative_positions) + 1
        else:
            positions[y][x] = -max(variations)


print('\n'.join(f'{i} - {pos}' for i, pos in enumerate(positions[s1][:limit-s1-1])))
