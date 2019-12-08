
DESIRED_OUTPUT = 19690720
MIN_VALUE = 0
MAX_VALUE = 99


def process(num_1=12, num_2=2):
    data = get_file_text()
    data[1] = num_1
    data[2] = num_2

    for index in range(0, len(data), 4):
        optcode = data[index]

        if optcode == 99:
            break

        pos_1 = data[index + 1]
        pos_2 = data[index + 2]
        pos_3 = data[index + 3]

        if optcode == 1:
            data[pos_3] = data[pos_1] + data[pos_2]
        elif optcode == 2:
            data[pos_3] = data[pos_1] * data[pos_2]

    return data[0]


def get_file_text():
    text = open('input.txt').read()
    return [int(item) for item in text.split(',')]


output = process()
print('Part 1: {}'.format(output))

for noun in range(MIN_VALUE, MAX_VALUE + 1):
    for verb in range(MIN_VALUE, MAX_VALUE + 1):
        result = process(num_1=noun, num_2=verb)

        if result != DESIRED_OUTPUT:
            continue

        print('Part 2: {}'.format(100 * noun + verb))
        break
