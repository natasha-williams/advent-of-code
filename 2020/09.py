
import common

from itertools import combinations


class XMAS(object):
    def __init__(self, numbers, preamble=25):
        self.numbers = numbers
        self.preamble = preamble

    @classmethod
    def from_data(cls, data):
        return cls(data)

    def run(self):
        index = self.preamble
        invalid_number = None

        while invalid_number is None:
            numbers = self.numbers[index - self.preamble:index]
            numbers = combinations(set(numbers), 2)
            number = self.numbers[index]
            is_valid = any(sum(item) == number for item in numbers)

            if not is_valid:
                invalid_number = number

            index += 1

        return invalid_number

    def get_contiguous(self, number, min_number=2):
        total = 0

        while total == 0:
            for item in zip(*(self.numbers[i:] for i in range(min_number))):
                if sum(item) == number:
                    total = min(item) + max(item)

            min_number += 1

        return total


data = common.get_lines(__file__)
xmas = XMAS.from_data(data)
invalid_number = xmas.run()

print('Part 1: {}'.format(invalid_number))
print('Part 2: {}'.format(xmas.get_contiguous(invalid_number)))
