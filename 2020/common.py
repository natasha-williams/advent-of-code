
def get_lines(name):
    name = name.split('.', 1)[0]
    text = open('{}.txt'.format(name)).read()
    data = [item for item in text.split('\n')]

    if data[0].isdigit():
        data = [int(item) for item in data]

    return data
