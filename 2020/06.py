
import common


class Person(object):
    def __init__(self, questions):
        self.questions = questions

    @classmethod
    def from_data(cls, data):
        questions = [item for item in data]
        return cls(questions)


class Group(object):
    def __init__(self, people):
        self.people = people

    @classmethod
    def from_data(cls, data):
        people = []

        for item in data:
            people.append([set(item) for item in item.split('\n')])

        return cls(people)

    def get_total(self, method):
        count = 0

        for item in self.people:
            count += len(method(*item))

        return count


data = common.get_lines(__file__, split='\n\n')
groups = Group.from_data(data)

print('Part 1: {}'.format(groups.get_total(method=set.union)))
print('Part 2: {}'.format(groups.get_total(method=set.intersection)))
