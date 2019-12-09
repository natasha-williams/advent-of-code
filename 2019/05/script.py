
OPTCODES_TO_PARAMS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0,
}


def get_instructions(data, index):
    value = str(data[index])
    optcode = int(value[-2:])
    num_params = OPTCODES_TO_PARAMS[optcode]
    modes = [int(item) for item in value[:-2]]

    modes.reverse()

    while len(modes) != num_params:
        modes.append(0)

    return optcode, get_params(data, modes, index)


def get_params(data, modes, index):
    params = []

    for num, mode in enumerate(modes):
        value = index + num + 1

        if not mode:
            value = data[value]

        params.append(value)

    return params


def process():
    data = get_items()
    index = 0

    while index < len(data):
        optcode, params = get_instructions(data, index)
        num = OPTCODES_TO_PARAMS[optcode]

        if optcode == 99:
            break

        if optcode == 1:
            data[params[2]] = data[params[0]] + data[params[1]]
        elif optcode == 2:
            data[params[2]] = data[params[0]] * data[params[1]]
        elif optcode == 3:
            data[params[0]] = input('ID: ')
        elif optcode == 4:
            print data[params[0]]
        elif optcode == 5 and data[params[0]]:
            index = data[params[1]]
            continue
        elif optcode == 6 and not data[params[0]]:
            index = data[params[1]]
            continue
        elif optcode == 7:
            data[params[2]] = int(data[params[0]] < data[params[1]])
        elif optcode == 8:
            data[params[2]] = int(data[params[0]] == data[params[1]])

        index += num + 1

    return data


def get_items():
    text = open('input.txt').read()
    return [int(item) for item in text.split(',')]


output = process()
