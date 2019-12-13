
class Image(object):
    COLOURS = {
        0: ' ',
        1: '1',
    }

    def __init__(self, data, width, height):
        self.data = data
        self.width = width
        self.height = height

    @classmethod
    def from_data(cls, width, height):
        text = open('input.txt').read()
        pixels = width * height
        data = [text[i:i + pixels] for i in range(0, len(text), pixels)]
        return cls(data, width, height)

    def get_totals(self, value):
        data = [[item.count(value), item] for item in self.data]
        data.sort()
        return data

    def get_layer_fewest(self, value):
        self.layer = self.get_totals(value)[0][1]
        return self.layer

    def get_count(self, value):
        return self.layer.count(value)

    def decode(self):
        data = []

        for index in range(self.height * self.width):
            pixels = [int(item[index]) for item in self.data]

            if index % self.width == 0:
                data.append('\n')

            for item in pixels:
                if item in self.COLOURS:
                    data.append(self.COLOURS[item])
                    break

        return ''.join(data)


image = Image.from_data(25, 6)
layer_fewest_zeros = image.get_layer_fewest('0')

print 'Part 1: {}'.format(image.get_count('1') * image.get_count('2'))
print 'Part 2: {}'.format(image.decode())
