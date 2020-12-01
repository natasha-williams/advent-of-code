
def get_lines(name):
    name = name.split('.', 1)[0]
    text = open('{}.txt'.format(name)).read()

    return [int(item) for item in text.split('\n')]
