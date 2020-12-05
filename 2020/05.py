
import common


class Seat(object):
    def __init__(self, data):
        self.data = [item for item in data]

    @classmethod
    def from_data(cls, data):
        return cls(data)

    def get_index(self, min_number, max_number, min_letter, max_letter):
        index = 0
        item = None

        while item is None:
            letter = self.data[index]
            value = round((max_number - min_number) / 2)

            if max_number - min_number == 1:
                if letter == min_letter:
                    item = min_number
                elif letter == max_letter:
                    item = max_number

            if letter == min_letter:
                max_number -= value
            elif letter == max_letter:
                min_number += value

            index += 1

        return item

    def get_seat_id(self):
        row = self.get_index(0, 127, 'F', 'B')
        column = self.get_index(0, 7, 'L', 'R')

        return row * 8 + column


data = common.get_lines(__file__)
ids = []

for item in data:
    seat = Seat.from_data(item)
    ids.append(seat.get_seat_id())

ids.sort()
seat_id = [x for x in range(ids[0], ids[-1]+1) if x not in ids][0]

print('Part 1: {}'.format(max(ids)))
print('Part 2: {}'.format(seat_id))
