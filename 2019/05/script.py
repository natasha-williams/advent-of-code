
from intcode import IntcodeGenerator


print('Part 1: {}'.format(IntcodeGenerator.from_data().run(1)))
print('Part 2: {}'.format(IntcodeGenerator.from_data().run(5)))
