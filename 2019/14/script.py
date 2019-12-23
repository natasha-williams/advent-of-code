
import math


class Reaction(object):
    def __init__(self, number, reference, data={}, value=0):
        self.number = number
        self.reference = reference
        self.data = data
        self.value = value
        self.remaining = 0

    @classmethod
    def from_ore(cls, number, reference, string):
        num, ref = string.strip().split(' ')
        return cls(number, reference, value=int(num))

    @classmethod
    def from_reaction(cls, number, reference, string):
        data = {}

        for item in string.split(', '):
            num, ref = item.strip().split(' ')
            data[ref] = int(num)

        return cls(number, reference, data)


class Reactions(object):
    def __init__(self, reactions, ores):
        self.reactions = reactions
        self.ores = ores
        self.need = {}

    @classmethod
    def from_data(cls):
        text = open('input.txt').read().split('\n')
        reactions = {}
        ores = {}

        for item in text:
            frm, to = item.split('=>')
            to_num, to_ref = to.strip().split(' ')
            to_num = int(to_num)

            if 'ORE' in item:
                ores[to_ref] = Reaction.from_ore(to_num, to_ref, frm)
            else:
                reactions[to_ref] = Reaction.from_reaction(to_num, to_ref, frm)

        return cls(reactions, ores)

    def reset(self):
        self.need = {}

        for item in self.reactions:
            self.reactions[item].remaining = 0

    def calculate(self, reaction, parent):
        for item in reaction.data:
            if item not in self.need:
                self.need[item] = []

            if item in self.ores:
                self.need[item].append(reaction.data[item] * parent)
            else:
                number = reaction.data[item] * parent
                number -= self.reactions[item].remaining
                total = math.ceil(number / float(self.reactions[item].number))
                total_have = total * self.reactions[item].number
                total_used = parent * reaction.data[item]
                self.reactions[item].remaining += total_have - total_used
                self.calculate(self.reactions[item], parent=total)

    def get_total_ore(self, fuel=1):
        total_ore = 0
        reaction = self.reactions['FUEL']

        self.calculate(reaction, parent=fuel)

        for item in self.need:
            if len(self.need[item]) == 0:
                continue

            ore = self.ores[item]
            total = math.ceil(sum(self.need[item]) / float(ore.number))
            total_ore += int(total) * ore.value

        self.reset()

        return total_ore

    def get_max_fuel(self, max_ore=1000000000000):
        total_ore = self.get_total_ore()
        fuel = max_ore / total_ore

        while True:
            ore = self.get_total_ore(fuel)
            fuel += (max_ore - ore) / total_ore

            if ore > max_ore:
                break

            fuel += 1

        return fuel


reactions = Reactions.from_data()

print 'Part 1: {}'.format(reactions.get_total_ore())
print 'Part 2: {}'.format(reactions.get_max_fuel())
