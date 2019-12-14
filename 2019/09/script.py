
import path

from intcode import LoopIntcodeGenerator


generator_1 = LoopIntcodeGenerator.from_data()
generator_2 = LoopIntcodeGenerator.from_data()

print 'Part 1: {}'.format(generator_1.run(1))
print 'Part 2: {}'.format(generator_2.run(2))
