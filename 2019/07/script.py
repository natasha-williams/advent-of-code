
import path

from itertools import permutations

from intcode import IntcodeGenerator, LoopIntcodeGenerator


def get_max_signal(phases, feedback_mode=False):
    signals = []

    for permutation in phases:
        cls = LoopIntcodeGenerator if feedback_mode else IntcodeGenerator
        generators = [cls.from_phase(item) for item in permutation]
        input_value = 0

        while not generators[-1].has_complete:
            for generator in generators:
                input_value = generator.run(input_value)

        signals.append(input_value)

    return max(signals)


phases_1 = permutations(range(0, 5))
phases_2 = permutations(range(5, 10))

print('Part 1: {}'.format(get_max_signal(phases_1)))
print('Part 2: {}'.format(get_max_signal(phases_2, feedback_mode=True)))
