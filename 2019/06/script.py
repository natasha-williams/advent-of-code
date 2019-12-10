
def get_orbits():
    data = get_items()
    sources = [x[0] for x in data]
    destinations = [x[1] for x in data]
    orbits = {item[1]: [] for item in data}

    for item in data:
        tmp_destination = destination = item[1]

        while tmp_destination in destinations:
            index = destinations.index(tmp_destination)
            tmp_destination = sources[index]
            orbits[destination].append(tmp_destination)

    return orbits


def get_total_orbits(orbits):
    return sum([len(orbits[key]) for key in orbits.keys()])


def get_total_transfers(orbits, src='YOU', dst='SAN'):
    total_transfers = 0

    for item in orbits[src]:
        if item in orbits[dst]:
            total_transfers += orbits[dst].index(item)
            break

        total_transfers += 1

    return total_transfers


def get_items():
    text = open('input.txt').read()
    return [item.split(')') for item in text.split('\n')]


orbits = get_orbits()

print('Part 1: {}'.format(get_total_orbits(orbits)))
print('Part 2: {}'.format(get_total_transfers(orbits)))
