
MAX_LENGTH = 6


def is_ascending(value):
    data = sorted(value)
    return ''.join(data) == value


def has_repeat(value, limit=None):
    data = []

    for item in set(value):
        data.append([x for x in value if x == item])

    groups = [len(item) for item in data]
    repeated_items = filter(lambda item: item > 1, groups)

    if limit is not None:
        repeated_items = filter(lambda item: item == 2, repeated_items)

    return len(repeated_items) > 0


def get_ranges():
    text = open('input.txt').read()
    return [int(item) for item in text.split('-')]


range_1, range_2 = get_ranges()
numbers = range(range_1, range_2)
total_valid = 0
total_consecutive_valid = 0

for item in numbers:
    value = str(item)

    if len(value) != MAX_LENGTH:
        continue

    if not is_ascending(value):
        continue

    if not has_repeat(value):
        continue

    total_valid += 1

    if has_repeat(value, limit=2):
        total_consecutive_valid += 1

print('Part 1: {}'.format(total_valid))
print('Part 2: {}'.format(total_consecutive_valid))
