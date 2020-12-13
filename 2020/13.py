
import common

from itertools import count


class Schedules(object):
    def __init__(self, schedules, earliest_timestamp):
        self.schedules = schedules
        self.earliest_timestamp = earliest_timestamp

    @classmethod
    def from_data(cls, data):
        earliest_timestamp = int(data[0])
        data = data[1].split(',')
        schedules = []

        for index, item in enumerate(data):
            if not item.isdigit():
                continue

            schedules.append((int(item), index))

        return cls(schedules, earliest_timestamp)

    def get_earliest_bus(self):
        timestamp = self.earliest_timestamp
        bus = None

        while bus is None:
            for item, index in self.schedules:
                num = timestamp / item

                if not num.is_integer():
                    continue

                bus = (timestamp - self.earliest_timestamp) * item

            timestamp += 1

        return bus

    def get_earliest_timestamp(self):
        step_index = 0
        step = 1

        for item, index in self.schedules:
            for num in count(step_index, step):
                if (num + index) % item:
                    continue

                step_index = num
                step *= item
                break

        return num


data = common.get_lines(__file__)
schedules = Schedules.from_data(data)

print('Part 1: {}'.format(schedules.get_earliest_bus()))
print('Part 2: {}'.format(schedules.get_earliest_timestamp()))
