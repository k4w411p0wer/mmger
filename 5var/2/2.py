from typing import Callable


def create_truth_table(
        func: Callable,
        depth: int = 4,
        values: list[int] = None
) -> None:
    if values is None:
        values = []
    elif len(values) == depth:
        res = func(*values)
        return print(*values, ' ', res) if res else None
    create_truth_table(func, depth, values + [0])
    create_truth_table(func, depth, values + [1])


create_truth_table(lambda x, y, z, w: x != y and (not y or not z) and (z or w))

'''
Result: 

0 1 0 1   1
1 0 0 1   1
1 0 1 0   1
1 0 1 1   1
'''