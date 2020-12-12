
import common

ACTION_FORWARD = 'F'
ACTION_LEFT = 'L'
ACTION_RIGHT = 'R'
DIRECTION_NORTH = 'N'
DIRECTION_EAST = 'E'
DIRECTION_SOUTH = 'S'
DIRECTION_WEST = 'W'
DIRECTIONS = (DIRECTION_NORTH, DIRECTION_EAST, DIRECTION_SOUTH, DIRECTION_WEST)


class Navigation(object):
    def __init__(self, actions=[], x=0, y=0, direction=DIRECTION_EAST):
        self.actions = actions
        self.direction = direction
        self.x = x
        self.y = y

        if len(actions) > 0:
            self.wp = Navigation(x=10, y=1)

    @classmethod
    def from_data(cls, data):
        actions = [[item[:1], int(item[1:])] for item in data]

        return cls(actions)

    def move(self, action, number):
        if action == DIRECTION_NORTH:
            self.y += number
        elif action == DIRECTION_EAST:
            self.x += number
        elif action == DIRECTION_SOUTH:
            self.y -= number
        elif action == DIRECTION_WEST:
            self.x -= number

    def get_manhattan_distance(self):
        for action, number in self.actions:
            if action in DIRECTIONS:
                self.move(action, number)
            elif action == ACTION_FORWARD:
                self.move(self.direction, number)
            else:
                num = int(number / 90)
                index = DIRECTIONS.index(self.direction)

                if action == ACTION_LEFT:
                    num = (index - num) % 4
                else:
                    num = (index + num) % 4

                self.direction = DIRECTIONS[num]

        return abs(self.x) + abs(self.y)

    def get_waypoint_manhattan_distance(self):
        for action, number in self.actions:
            if action in DIRECTIONS:
                self.wp.move(action, number)
            elif action == ACTION_FORWARD:
                self.x += self.wp.x * number
                self.y += self.wp.y * number
            else:
                if action == ACTION_LEFT:
                    number = -number + 360

                if number == 90:
                    self.wp.x, self.wp.y = self.wp.y, -self.wp.x
                elif number == 180:
                    self.wp.x, self.wp.y = -self.wp.x, -self.wp.y
                elif number == 270:
                    self.wp.x, self.wp.y = -self.wp.y, self.wp.x

        return abs(self.x) + abs(self.y)


data = common.get_lines(__file__)
nav = Navigation.from_data(data)

print('Part 1: {}'.format(nav.get_manhattan_distance()))
print('Part 2: {}'.format(nav.get_waypoint_manhattan_distance()))
