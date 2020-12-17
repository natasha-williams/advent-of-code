
import common

ACTIVE = '#'
INACTIVE = '.'


class Dimension(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    @classmethod
    def from_data(cls, data):
        coordinates = {}

        for x, item in enumerate(data):
            for y, char in enumerate(item):
                coordinates[(x, y, 0, 0)] = char

        return cls(coordinates)

    def get_neighbours(self, item, is_hypercube):
        neighbours = set()
        ranges = range(-1, 2)
        x, y, z, w = item

        for xx in ranges:
            for yy in ranges:
                for zz in ranges:
                    if is_hypercube:
                        for ww in ranges:
                            if xx == 0 and yy == 0 and zz == 0 and ww == 0:
                                continue

                            neighbours.add((x + xx, y + yy, z + zz, w + ww))
                    else:
                        if xx == 0 and yy == 0 and zz == 0:
                            continue

                        neighbours.add((x + xx, y + yy, z + zz, 0))

        return neighbours

    def get_state(self, item):
        state = INACTIVE

        if item in self.coordinates:
            state = self.coordinates[item]

        return state

    def get_states(self, data, dimensions=3):
        return [self.get_state(item) for item in data]

    def run(self, cycles=6, is_hypercube=False):
        for index in range(cycles):
            new_coordinates = {}
            coordinates = set()

            for item in self.coordinates:
                neighbours = self.get_neighbours(item, is_hypercube)
                coordinates.add(item)
                coordinates = coordinates.union(neighbours)

            for item in coordinates:
                state = self.get_state(item)
                neighbours = self.get_neighbours(item, is_hypercube)
                total = self.get_states(neighbours).count(ACTIVE)

                if state == ACTIVE and (total != 2 and total != 3):
                    new_coordinates[item] = INACTIVE
                elif state == INACTIVE and total == 3:
                    new_coordinates[item] = ACTIVE
                else:
                    new_coordinates[item] = state

            self.coordinates = new_coordinates

        return list(self.coordinates.values()).count(ACTIVE)


data = common.get_lines(__file__)
dimension = Dimension.from_data(data)

print('Part 1: {}'.format(dimension.run()))
print('Part 2: {}'.format(dimension.run(is_hypercube=True)))
