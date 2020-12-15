
import common


class MemoryGame(object):
    def __init__(self, numbers):
        self.numbers = numbers

    @classmethod
    def from_data(cls, data):
        return cls(data)

    def run(self, rounds):
        cache = {}
        index = 0

        for item in self.numbers[:-1]:
            cache[item] = self.numbers.index(item)

        number = self.numbers[-1]
        index = len(self.numbers) - 1

        while index < rounds - 1:
            if number not in cache:
                cache[number] = index
                number = 0
            else:
                diff = (index + 1) - (cache[number] + 1)
                cache[number] = index
                number = diff

            index += 1

        return number


data = common.get_lines(__file__, split=',')
game = MemoryGame.from_data(data)

print('Part 1: {}'.format(game.run(2020)))
print('Part 2: {}'.format(game.run(30000000)))
