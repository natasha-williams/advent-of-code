
import utils


def get_increases(size=1):
    data = utils.get_data(__file__, data_type=int)
    data = [sum(data[i: i + size]) for i, x in enumerate(data) if len(data) >= i + size]
    num = 0

    for index, item in enumerate(data):
        if index == 0:
            continue

        if item > data[index - 1]:
            num += 1

    return num


print('Part 1: {}'.format(get_increases()))
print('Part 2: {}'.format(get_increases(size=3)))