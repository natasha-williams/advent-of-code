
import common

from functools import reduce


class Tickets(object):
    def __init__(self, rules, tickets):
        self.rules = rules
        self.tickets = tickets

    @classmethod
    def from_data(cls, data):
        data = [item.split('\n') for item in data]
        rules = {}
        tickets = {}

        for item in data[0]:
            name, values = item.split(': ')
            values = values.split(' or ')
            rules[name] = []

            for value in values:
                start, end = map(int, value.split('-'))
                rules[name] += range(start, end + 1)

        for item in data[2][1:] + data[1][1:]:
            values = list(map(int, item.split(',')))

            for index, value in enumerate(values):
                if index not in tickets:
                    tickets[index] = []

                tickets[index].append(value)

        return cls(rules, tickets)

    def get_invalid(self):
        rules = [x for rule in self.rules.values() for x in rule]
        invalid_indexes = []
        invalid_values = []

        for item in self.tickets:
            ticket = self.tickets[item]
            items = {idx: x for idx, x in enumerate(ticket) if x not in rules}

            if len(items) > 0:
                invalid_indexes += items.keys()
                invalid_values += items.values()

        invalid_indexes = list(set(invalid_indexes))
        invalid_indexes.sort()
        invalid_indexes.reverse()

        for index in invalid_indexes:
            for item in self.tickets:
                self.tickets[item].pop(index)

        return sum(invalid_values)

    def get_possible_rules(self):
        tickets = {}

        for item in self.tickets:
            ticket = self.tickets[item]

            if item not in tickets:
                tickets[item] = []

            for rule in self.rules:
                difference = len(set(ticket).difference(self.rules[rule]))

                if difference > 0:
                    continue

                tickets[item].append(rule)

        return tickets

    def get_ticket(self, key='departure'):
        self.get_invalid()
        rules = self.get_possible_rules()
        indexes = sorted(rules, key=lambda x: len(rules[x]))
        ticket = {}

        for index in indexes:
            for item in rules[index]:
                if item in ticket.keys() or not item.startswith(key):
                    continue

                ticket[item] = self.tickets[index][-1]

        return reduce(lambda x, y: x * y, ticket.values())


data = common.get_lines(__file__, split='\n\n')
tickets = Tickets.from_data(data)

print('Part 1: {}'.format(tickets.get_invalid()))
print('Part 2: {}'.format(tickets.get_ticket()))
