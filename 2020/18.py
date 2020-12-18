
import common

ACTION_ADD = '+'


class MathHomework(object):
    def __init__(self, calculations, is_advanced):
        self.calculations = calculations
        self.is_advanced = is_advanced

    @classmethod
    def from_data(cls, data, is_advanced=False):
        return cls(data, is_advanced)

    def process_parentheses(self, item):
        while ')' in item:
            c_index = item.index(')')
            total = len(item[:c_index])
            o_index = total - item[:c_index][::-1].index('(') - 1
            text = item[o_index:c_index + 1]
            calc = self.get_value(text[1:-1])
            item = item.replace(text, str(calc))

        return item

    def get_value(self, item):
        item = item.split(' ')

        if self.is_advanced:
            while ACTION_ADD in item:
                index = item.index(ACTION_ADD)
                number_1 = int(item[index - 1])
                number_2 = int(item[index + 1])

                del item[index - 1:index + 1]
                item[index - 1] = number_1 + number_2

        while len(item) > 1:
            number_1 = int(item[0])
            expression = item[1]
            number_2 = int(item[2])
            number = 0

            if expression == ACTION_ADD:
                number = number_1 + number_2
            else:
                number = number_1 * number_2

            item = item[2:]
            item[0] = number

        return item[0]

    def run(self):
        calculations = []

        for item in self.calculations:
            item = self.process_parentheses(item)
            calculations.append(self.get_value(item))

        return sum(calculations)


data = common.get_lines(__file__)
homework_1 = MathHomework.from_data(data)
homework_2 = MathHomework.from_data(data, is_advanced=True)

print('Part 1: {}'.format(homework_1.run()))
print('Part 2: {}'.format(homework_2.run()))
