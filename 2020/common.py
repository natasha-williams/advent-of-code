
def get_lines(name, split='\n'):
    name = name.split('.', 1)[0]
    text = open('{}.txt'.format(name)).read()
    data = [item for item in text.split(split)]

    if data[0].isdigit():
        data = [int(item) for item in data]

    return data
