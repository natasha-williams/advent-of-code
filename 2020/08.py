
import common


class Console(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0

    @classmethod
    def from_data(cls, data):
        instructions = []

        for item in data:
            instruction, number = item.split(' ')
            instructions.append({
                'instruction': instruction,
                'number': int(number),
                'has_run': False
            })

        return cls(instructions)

    def get_forced_accumulator(self, instructions=None, only_graceful=False):
        if instructions is None:
            instructions = [dict(item) for item in self.instructions]

        index = 0
        accumulator = 0
        is_graceful = False

        while True:
            if index >= len(instructions):
                is_graceful = True
                break

            if instructions[index]['has_run']:
                break

            if instructions[index]['instruction'] == 'acc':
                accumulator += instructions[index]['number']
            elif instructions[index]['instruction'] == 'jmp':
                index += instructions[index]['number']
                continue

            instructions[index]['has_run'] = True
            index += 1

        return None if only_graceful and not is_graceful else accumulator

    def get_fixed_accumulator(self):
        accumulator = None

        for index, item in enumerate(self.instructions):
            instructions = [dict(item) for item in self.instructions]

            if instructions[index]['instruction'] == 'jmp':
                instructions[index]['instruction'] = 'nop'

            accumulator = self.get_forced_accumulator(instructions,
                                                      only_graceful=True)

            if accumulator is not None:
                break

        return accumulator


data = common.get_lines(__file__)
console = Console.from_data(data)

print('Part 1: {}'.format(console.get_forced_accumulator()))
print('Part 2: {}'.format(console.get_fixed_accumulator()))
