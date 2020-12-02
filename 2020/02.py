
import common


class PasswordPolicy(object):
    def __init__(self, password, letter, num_1, num_2):
        self.password = password
        self.letter = letter
        self.num_1 = num_1
        self.num_2 = num_2

    @classmethod
    def from_data(cls, data):
        policy, password = data.split(': ')
        numbers, letter = policy.split(' ')
        num_1, num_2 = map(int, numbers.split('-'))

        return cls(password, letter, num_1, num_2)

    def is_valid_occurances(self):
        count = self.password.count(self.letter)

        return count >= self.num_1 and count <= self.num_2

    def is_valid_indexes(self):
        nums = [self.num_1, self.num_2]
        data = [int(self.password[item - 1] == self.letter) for item in nums]

        return sum(data) == 1


data = common.get_lines(__file__)
count_occurances = 0
count_indexes = 0

for item in data:
    password = PasswordPolicy.from_data(item)

    if password.is_valid_occurances():
        count_occurances += 1

    if password.is_valid_indexes():
        count_indexes += 1

print('Part 1: {}'.format(count_occurances))
print('Part 2: {}'.format(count_indexes))
