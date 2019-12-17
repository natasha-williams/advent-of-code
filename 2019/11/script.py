
import path

from intcode import LoopIntcodeGenerator


class Image(object):
    DIRECTIONS = {
        0: 'up',
        1: 'right',
        2: 'down',
        3: 'left',
    }

    def __init__(self, generator):
        self.generator = generator
        self.direction = 0
        self.data = {}

    @classmethod
    def from_generator(cls):
        generator = LoopIntcodeGenerator.from_data()
        return cls(generator)

    def set_direction(self, direction):
        if direction == 0:
            self.direction -= 1
        else:
            self.direction += 1

        self.direction = self.direction % 4

    def up(self, x, y):
        return x, y + 1

    def right(self, x, y):
        return x + 1, y

    def down(self, x, y):
        return x, y - 1

    def left(self, x, y):
        return x - 1, y

    def coorinates(self, start_colour=0):
        x = y = 0

        while not self.generator.has_complete:
            xy = (x, y)
            colour = self.data[xy] if xy in self.data else start_colour
            self.data[xy] = self.generator.run(colour)
            direction = self.generator.run()
            self.set_direction(direction)
            x, y = getattr(self, self.DIRECTIONS[self.direction])(x, y)

    def draw(self, colour=1):
        data = []
        all_x = [item[0] for item in self.data]
        all_y = [item[1] for item in self.data]
        range_x = range(min(all_x), max(all_x) + 1)
        range_y = reversed(range(min(all_y), max(all_y) + 1))

        for y in range_y:
            data.append('\n')

            for x in range_x:
                xy = (x, y)
                pixel_colour = -1

                if xy in self.data:
                    pixel_colour = self.data[xy]

                pixel_colour = '#' if pixel_colour == colour else ' '
                data.append(pixel_colour)

        return ''.join(data)


image_1 = Image.from_generator()
image_1.coorinates()
image_2 = Image.from_generator()
image_2.coorinates(start_colour=1)

print 'Part 1: {}'.format(len(image_1.data))
print 'Part 2: {}'.format(image_2.draw())
