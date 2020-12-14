
import common

from itertools import product


class DockingProgram(object):
    def __init__(self, commands):
        self.commands = commands

    @classmethod
    def from_data(cls, data):
        commands = {}

        for item in data:
            if 'mask' in item:
                mask = item.split(' = ')[1]
                commands[mask] = []
            else:
                index, num = item.split(' = ')
                index = index.replace('mem[', '').replace(']', '')
                commands[mask].append((int(index), int(num)))

        return cls(commands)

    def run(self, cmds=[]):
        numbers = {}
        commands = cmds
        skip_opts = ('X', '1')

        if not cmds:
            commands = self.commands
            skip_opts = ('0', '1')

        for mask in commands:
            original_mask = [item for item in mask]
            original_mask.reverse()

            for index, item in commands[mask]:
                num = [x for x in bin(item)[2:]]
                mask = list(original_mask)

                if not cmds:
                    mask = [x.replace('X', '0') for x in mask]

                num.reverse()

                for idx, num in enumerate(num):
                    if original_mask[idx] in skip_opts:
                        continue

                    mask[idx] = num

                mask.reverse()
                numbers[index] = ''.join(mask)

        return numbers

    def get_total(self):
        return sum([int(item, 2) for item in self.run().values()])

    def get_variant_total(self):
        commands = dict(self.commands)
        numbers = {}

        for mask in commands:
            commands[mask] = [(item, index) for index, item in commands[mask]]

        for item, mask in self.run(commands).items():
            for variant in product(('0', '1'), repeat=mask.count('X')):
                mask_item = list(mask)

                for num in variant:
                    mask_item[mask_item.index('X')] = num

                value = int(''.join(mask_item), 2)
                numbers[value] = item

        return sum(numbers.values())


data = common.get_lines(__file__)
program = DockingProgram.from_data(data)

print('Part 1: {}'.format(program.get_total()))
print('Part 2: {}'.format(program.get_variant_total()))
