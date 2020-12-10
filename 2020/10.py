
import common

MAX_JOLTS = 3


class Adapter(object):
    def __init__(self, jolt, total_paths=0):
        self.jolt = jolt
        self.total_paths = total_paths

    def get_jolts(self):
        return [self.jolt + item for item in range(1, MAX_JOLTS + 1)]


class Adapters(object):
    def __init__(self, adapters):
        self.adapters = adapters
        self.data = {item.jolt: item for item in adapters}

    @classmethod
    def from_data(cls, data):
        data.sort()

        adapters = [Adapter(item) for item in data]
        adapters.insert(0, Adapter(0, total_paths=1))
        adapters.append(Adapter(max(data) + MAX_JOLTS))

        return cls(adapters)

    def get_joltage_difference(self):
        outlet_joltage = 0
        differences = []

        for item in self.adapters:
            num = next((x for x in item.get_jolts() if x in self.data), None)

            if num is None:
                break

            differences.append(num - outlet_joltage)
            outlet_joltage = num

        return differences.count(1) * differences.count(3)

    def get_total_paths(self):
        for adapter in self.adapters:
            for item in adapter.get_jolts():
                if item not in self.data:
                    continue

                self.data[item].total_paths += adapter.total_paths

        return self.adapters[-1].total_paths


data = common.get_lines(__file__)
adapters = Adapters.from_data(data)

print('Part 1: {}'.format(adapters.get_joltage_difference()))
print('Part 2: {}'.format(adapters.get_total_paths()))
