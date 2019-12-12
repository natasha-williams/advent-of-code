
class IntcodeGenerator(object):
    MAX_DIGITS = 5
    OPTCODE_EXIT_MODES = (99,)
    OPTCODE_MODES = {
        1: ['add', 4],
        2: ['multiply', 4],
        3: ['replace', 2],
        4: ['set_output', 2],
        5: ['jump_if_true', 3],
        6: ['jump_if_false', 3],
        7: ['is_less_than', 4],
        8: ['is_equal', 4],
        99: ['exit', 0],
    }

    def __init__(self, data, phase):
        self.index = 0
        self.data = data
        self.phase = phase
        self.number = None
        self.output = None
        self.has_complete = False

    @classmethod
    def from_data(cls, phase=None):
        data = [int(item) for item in open('input.txt').read().split(',')]
        return cls(data, phase)

    @classmethod
    def from_phase(cls, phase):
        phase = int(phase)
        return cls.from_data(phase)

    def get_instructions(self):
        instruction = str(self.data[self.index]).zfill(self.MAX_DIGITS)
        optcode = int(instruction[-2:])
        instructions = []

        for i, item in enumerate(instruction[::-1][2:]):
            idx = self.index + i + 1
            total = len(self.data)
            value = idx if int(item) or idx >= total else self.data[idx]
            instructions.append(value)

        return [optcode] + instructions

    def add(self, *args):
        self.data[args[2]] = self.data[args[0]] + self.data[args[1]]
        self.index += args[3]

    def multiply(self, *args):
        self.data[args[2]] = self.data[args[0]] * self.data[args[1]]
        self.index += args[3]

    def set_output(self, *args):
        self.output = self.data[args[0]]
        self.index += args[3]

    def replace(self, *args):
        if self.phase is not None:
            self.data[args[0]] = self.phase
            self.phase = None
        else:
            self.data[args[0]] = self.number

        self.index += args[3]

    def jump_if_true(self, *args):
        if self.data[args[0]] > 0:
            self.index = self.data[args[1]]
        else:
            self.index += args[3]

    def jump_if_false(self, *args):
        if self.data[args[0]] == 0:
            self.index = self.data[args[1]]
        else:
            self.index += args[3]

    def is_less_than(self, *args):
        self.data[args[2]] = int(self.data[args[0]] < self.data[args[1]])
        self.index += args[3]

    def is_equal(self, *args):
        self.data[args[2]] = int(self.data[args[0]] == self.data[args[1]])
        self.index += args[3]

    def exit(self, *args):
        self.has_complete = True

    def run(self, number):
        self.number = number

        while True:
            optcode, param_1, param_2, param_3 = self.get_instructions()
            fn, num_params = self.OPTCODE_MODES[optcode]
            getattr(self, fn)(param_1, param_2, param_3, num_params)

            if optcode in self.OPTCODE_EXIT_MODES:
                break

        return self.output
