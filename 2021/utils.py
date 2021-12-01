
def get_data(name, *, data_type=str, split_at='\n'):
    name = name.split('.', 1)[0]
    text = open('{}.txt'.format(name)).read()
    return list(map(data_type, [item for item in text.split(split_at)]))
