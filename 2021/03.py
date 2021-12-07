
import utils


class Submarine(object):
    RATINGS = {
        'o2': ('0', '1'),
        'co2': ('1', '0'),
    }

    def __init__(self, data):
        self.data = data
        self.gamma_rate = ''
        self.epsilon_rate = ''

    @classmethod
    def from_data(cls):
        return cls(utils.get_data(__file__))

    def report(self):
        for item in zip(*self.data):
            if item.count('0') > item.count('1'):
                self.gamma_rate += '0'
                self.epsilon_rate += '1'
            else:
                self.gamma_rate += '1'
                self.epsilon_rate += '0'

        return int(self.gamma_rate, 2) * int(self.epsilon_rate, 2)

    def get_rating(self, *, rating='o2'):
        data = list(map(list, zip(*self.data)))
        less_bit, more_bit = self.RATINGS[rating]

        for item in data:
            bit = more_bit if item.count('0') > item.count('1') else less_bit
            indexes = sorted([i for i, x in enumerate(item) if x == bit],
                             reverse=True)

            for index in indexes:
                for a in data:
                    del a[index]

            if len(item) == 1:
                break

        return int(''.join([x[0] for x in data]), 2)


submarine = Submarine.from_data()
print('Part 1: {}'.format(submarine.report()))
print('Part 2: {}'.format(submarine.get_rating() * submarine.get_rating(rating='co2')))
