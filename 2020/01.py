
from functools import reduce
from itertools import combinations

import common

SUM_TOTAL = 2020


def get_combinations(amount):
    data = common.get_lines(__file__)
    number = 0

    for item in combinations(data, amount):
        if sum(item) == SUM_TOTAL:
            number = reduce(lambda x, y: x * y, item)
            break

    return number


print('Part 1: {}'.format(get_combinations(2)))
print('Part 2: {}'.format(get_combinations(3)))
