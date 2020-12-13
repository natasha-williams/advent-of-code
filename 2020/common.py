
def get_lines(name, split='\n'):
    name = name.split('.', 1)[0]
    text = open('{}.txt'.format(name)).read()
    data = [item for item in text.split(split)]
    is_digit = len([item for item in data if item.isdigit()]) == len(data)

    if is_digit:
        data = [int(item) for item in data]

    return data
