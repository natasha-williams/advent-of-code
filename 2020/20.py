
import common

from functools import reduce


class Tile(object):
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile.split('\n')

    def get_combinations(self):
        combinations = [self.tile]

        for index in range(3):
            item = list(map(''.join, zip(*reversed(combinations[-1]))))
            combinations.append(item)

        for tile in list(combinations):
            item = [x[::-1]for x in tile]
            combinations.append(item)

        return combinations

    def get_edges(self):
        edges = []

        for item in self.get_combinations():
            items = set()
            items.add(item[0])
            items.add(item[-1])
            items.add(''.join([x[0] for x in item]))
            items.add(''.join([x[-1] for x in item]))

            edges.append(items)

        return edges

    def find(self, tiles):
        items = set()
        my_edges = self.get_edges()

        for item in tiles:
            if self.id == item:
                continue

            edges = tiles[item].get_edges()

            for my_edge in my_edges:
                for edge in edges:
                    values = my_edge.intersection(edge)

                    if len(values) > 0:
                        items.add(item)

        return items


class Tiles(object):
    def __init__(self, tiles):
        self.tiles = tiles

    @classmethod
    def from_data(cls, data):
        tiles = {}

        for item in data:
            number, tile = item.split(':\n')
            number = int(number.replace('Tile ', ''))
            tiles[number] = Tile(number, tile)

        return cls(tiles)

    def get_corners(self):
        data = {}

        for item in self.tiles:
            data[item] = self.tiles[item].find(self.tiles)

        corners = [item for item in data if len(data[item]) == 2]

        return reduce(lambda x, y: x * y, corners)


data = common.get_lines(__file__, split='\n\n')
tiles = Tiles.from_data(data)

print('Part 1: {}'.format(tiles.get_corners()))
