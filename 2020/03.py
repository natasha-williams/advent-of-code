
import common

DIRECTION_RIGHT = 'right'
DIRECTION_DOWN = 'down'


class RoutePlanner(object):
    def __init__(self, routes, right, down):
        self.routes = routes
        self.path = []
        self.right = right
        self.down = down
        self.index = {
            DIRECTION_RIGHT: 0,
            DIRECTION_DOWN: 0
        }

    @classmethod
    def from_data(cls, data, right, down):
        routes = []

        for item in data:
            routes.append([x for x in item])

        return cls(routes, right, down)

    def move(self, direction, num):
        index = self.index[direction] + num
        total = len(self.routes[self.index[DIRECTION_DOWN]])

        if direction == DIRECTION_RIGHT and index >= total:
            index -= total

        self.index[direction] = index

    def set_path(self):
        index_bottom = self.index[DIRECTION_DOWN]
        index_right = self.index[DIRECTION_RIGHT]
        self.path.append(self.routes[index_bottom][index_right])

    def get_total_trees(self):
        while self.index[DIRECTION_DOWN] < len(self.routes) - 1:
            self.move(DIRECTION_RIGHT, self.right)
            self.move(DIRECTION_DOWN, self.down)
            route.set_path()

        return self.path.count('#')


data = common.get_lines(__file__)
route = RoutePlanner.from_data(data, 3, 1)

print('Part 1: {}'.format(route.get_total_trees()))

routes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
count = 1

for right, down in routes:
    route = RoutePlanner.from_data(data, right, down)
    count = count * route.get_total_trees()

print('Part 2: {}'.format(count))
