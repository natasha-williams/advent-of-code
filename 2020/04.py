
import common

VALID_EYE_COLOURS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
REQUIRED_FIELDS = {
    'byr': lambda x: is_valid_range(x, 1920, 2002),
    'iyr': lambda x: is_valid_range(x, 2010, 2020),
    'eyr': lambda x: is_valid_range(x, 2020, 2030),
    'hgt': lambda x: (x.endswith('cm') and is_valid_range(x[:-2], 150, 193)) or
                     (x.endswith('in') and is_valid_range(x[:-2], 59, 76)),
    'hcl': lambda x: x.startswith('#') and len(x) == 7 and x[1:].isalnum(),
    'ecl': lambda x: x in VALID_EYE_COLOURS,
    'pid': lambda x: len(x) == 9 and x.isdigit()
}


class Passport(object):
    def __init__(self, fields):
        self.fields = fields

    @classmethod
    def from_data(cls, data):
        data = data.replace('\n', ' ').split(' ')
        fields = {}

        for item in data:
            key, value = item.split(':')

            if key not in REQUIRED_FIELDS.keys():
                continue

            fields[key] = value

        return cls(fields)

    def is_valid(self, check_values):
        is_valid = not REQUIRED_FIELDS.keys() - self.fields.keys()

        if check_values and is_valid:
            for item in REQUIRED_FIELDS.keys():
                if not is_valid:
                    break

                is_valid = REQUIRED_FIELDS[item](self.fields[item])

        return is_valid


class Scanner(object):
    def __init__(self, entries):
        self.entries = entries

    @classmethod
    def from_data(cls, data):
        entries = [Passport.from_data(item) for item in data]

        return cls(entries)

    def count_valid(self, check_values=False):
        count = 0

        for item in self.entries:
            if item.is_valid(check_values):
                count += 1

        return count


def is_valid_range(value, min, max):
    return int(value) >= min and int(value) <= max


data = common.get_lines(__file__, split='\n\n')
scanner = Scanner.from_data(data)

print('Part 1: {}'.format(scanner.count_valid()))
print('Part 2: {}'.format(scanner.count_valid(check_values=True)))
