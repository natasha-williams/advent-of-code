
import common


class Luggage(object):
    def __init__(self, bags):
        self.bags = bags
        self.rules = bags

    @classmethod
    def from_data(cls, data):
        bags = {}

        for item in data:
            item = item.replace('bags', '').replace(
                'bag', '').replace('.', '').replace('no other', '').strip()
            colour, item = item.split('contain')
            bags[colour.strip()] = [x.strip() for x in item.split(',') if x]

        return cls(bags)

    def get_total_rules(self, colour, rules=None):
        count = 0

        if rules is None:
            rules = dict(self.rules)

        for item in self.rules:
            if not any(colour in x for x in rules[item]):
                continue

            rules[item] = []
            count += 1
            count += self.get_total_rules(item, rules)

        return count

    def get_total_bags(self, colour):
        count = 0

        for item in self.rules[colour]:
            number, colour = item.split(' ', 1)
            count += int(number) * (1 + self.get_total_bags(colour))

        return count


data = common.get_lines(__file__)
luggage = Luggage.from_data(data)

print('Part 1: {}'.format(luggage.get_total_rules('shiny gold')))
print('Part 2: {}'.format(luggage.get_total_bags('shiny gold')))
