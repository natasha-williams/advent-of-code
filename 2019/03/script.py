
DIRECTIONS = {
    'x': ['R', 'L'],
    'y': ['U', 'D'],
}


def format_coordinates(data):
    return [[item[0], int(item[1:])] for item in data]


def get_coordinates(data):
    coordinates = {}
    x = 0
    y = 0
    steps = 0

    for direction, distance in format_coordinates(data):
        for number in range(distance):
            steps += 1

            if direction in DIRECTIONS['x']:
                if direction == DIRECTIONS['x'][0]:
                    x += 1
                else:
                    x -= 1
            else:
                if direction == DIRECTIONS['y'][0]:
                    y += 1
                else:
                    y -= 1

            coordinates[(x, y)] = steps

    return coordinates


def get_duplicates(line_1, line_2):
    return set(line_1.keys()) & set(line_2.keys())


def get_closest(data):
    sum_data = [abs(x) + abs(y) for x, y in data]
    return min(sum_data)


def get_min_steps(data):
    sum_data = [line_1[item] + line_2[item] for item in data]
    return min(sum_data)


def get_lines():
    text = open('input.txt').read()
    return [get_coordinates(item.split(',')) for item in text.split('\n')]


line_1, line_2 = get_lines()
duplicates = get_duplicates(line_1, line_2)

print('Part 1: {}'.format(get_closest(duplicates)))
print('Part 2: {}'.format(get_min_steps(duplicates)))
