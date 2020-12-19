
import re

import common

FIX = {
    '8': '42 | 42 8',
    '11': '42 31 | 42 11 31'
}


class Messages(object):
    def __init__(self, rules, messages):
        self.rules = rules
        self.messages = messages

    @classmethod
    def from_data(cls, data):
        rules = {}

        for item in data[0].split('\n'):
            number, rule = item.split(': ')
            items = rule.split('"')

            if len(items) > 1:
                rules[number] = items[1]
            else:
                rules[number] = rule.split(' ')

        return cls(rules, data[1].split('\n'))

    def process(self, rules):
        for item in self.rules:
            rule = self.rules[item]
            regex = ''

            if type(rule) == str:
                rules[item] = rule
                continue

            is_complete = all(x == '|' or x in rules for x in rule)

            if not is_complete:
                continue

            for x in rule:
                if x in rules:
                    regex += rules[x]
                else:
                    regex += x

            rules[item] = '(' + regex + ')'

        return rules

    def check(self, id, with_fix=False):
        rules = {}
        count = 0

        while id not in rules.keys():
            rules = self.process(rules)

        if with_fix:
            return self.check_with_fix(rules, id)

        for item in self.messages:
            if re.fullmatch(rules[id], item):
                count += 1

        return count

    def check_with_fix(self, rules, id):
        messages = []

        for item in FIX:
            self.rules[item] = FIX[item].split(' ')

        while True:
            total = len(messages)
            rules.update(self.process(rules))

            for item in self.messages:
                if item not in messages and re.fullmatch(rules[id], item):
                    messages.append(item)

            if total == len(messages):
                break

        return len(messages)


data = common.get_lines(__file__, split='\n\n')
messages = Messages.from_data(data)

print('Part 1: {}'.format(messages.check('0')))
print('Part 2: {}'.format(messages.check('0', with_fix=True)))
