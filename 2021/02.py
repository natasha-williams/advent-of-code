
import utils


class Submarine(object):
    DIRECTIONS = {
        'up': (0, -1, 0),
        'down': (0, 1, 0),
        'forward': (1, 0, 1),
    }

    def __init__(self, data):
        self.data = data

    def reset(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    @classmethod
    def from_data(cls):
        data = [x.split() for x in utils.get_data(__file__)]
        return cls([(x[0], int(x[1])) for x in data])

    def drive(self, calculate_aim=False):
        self.reset()

        for direction, amount in self.data:
            depth = self.DIRECTIONS[direction][1] * amount

            if calculate_aim:
                self.aim += self.DIRECTIONS[direction][1] * amount
                depth = self.aim * (self.DIRECTIONS[direction][2] * amount)

            self.horizontal += self.DIRECTIONS[direction][0] * amount
            self.depth += depth

        return self.horizontal * self.depth

submarine = Submarine.from_data()
print('Part 1: {}'.format(submarine.drive()))
print('Part 1: {}'.format(submarine.drive(calculate_aim=True)))
