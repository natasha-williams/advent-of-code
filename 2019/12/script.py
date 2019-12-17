
from itertools import combinations


class Position(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Moon(object):
    def __init__(self, position):
        self.position = Position(position[0], position[1], position[2])
        self.velocity = Position()

    def set_velocity(self, moon):
        for item in vars(self.velocity).keys():
            pos_1 = getattr(self.position, item)
            pos_2 = getattr(moon.position, item)

            if pos_1 > pos_2:
                self.decrease_velocity(item)
                moon.increase_velocity(item)
            elif pos_2 > pos_1:
                self.increase_velocity(item)
                moon.decrease_velocity(item)

    def decrease_velocity(self, axis):
        setattr(self.velocity, axis, getattr(self.velocity, axis) - 1)

    def increase_velocity(self, axis):
        setattr(self.velocity, axis, getattr(self.velocity, axis) + 1)

    def set_positions(self):
        for item in vars(self.velocity).keys():
            value = getattr(self.position, item) + getattr(self.velocity, item)
            setattr(self.position, item, value)

    def get_potential_energy(self):
        return sum(abs(item) for item in vars(self.position).values())

    def get_kinetic_energy(self):
        return sum(abs(item) for item in vars(self.velocity).values())


class Moons(object):
    AXIS = ['x', 'y', 'z']

    def __init__(self, moons):
        self.moons = moons

    @classmethod
    def from_data(cls):
        text = open('input.txt').read().replace('<', '').replace('>', '')
        data = [item.split(', ') for item in text.split('\n')]
        moons = []

        for item in data:
            moon = [int(x.split('=')[1]) for x in item]
            moons.append(Moon(moon))

        return cls(moons)

    def get_values(self, axis):
        data = []

        for moon in self.moons:
            data.append(getattr(moon.position, axis))
            data.append(getattr(moon.velocity, axis))

        return tuple(data)

    def time_step(self, step=1):
        for index in range(step):
            for moons in combinations(self.moons, 2):
                moons[0].set_velocity(moons[1])

            for moon in self.moons:
                moon.set_positions()

    def get_energy(self):
        energy = 0

        for moon in self.moons:
            energy += moon.get_potential_energy() * moon.get_kinetic_energy()

        return energy

    def lcm(self, item_1, item_2):
        value = (item_1 * item_2)

        while item_2:
            item_1, item_2 = item_2, item_1 % item_2

        return value / item_1

    def get_match_step(self):
        repeats = [0, 0, 0]
        step = 0
        initial = {}

        for item in self.AXIS:
            initial[self.get_values(item)] = item

        items = initial.keys()
        items.sort()

        for index, key in enumerate(items):
            axis = initial[key]

            while True:
                self.time_step()
                step += 1

                if repeats[index] == 0 and self.get_values(axis) == key:
                    repeats[index] = step
                    break

        num = self.lcm(repeats[0], repeats[1])
        return self.lcm(num, repeats[2])


moons_1 = Moons.from_data()
moons_1.time_step(step=1000)
moons_2 = Moons.from_data()

print 'Part 1: {}'.format(moons_1.get_energy())
print 'Part 2: {}'.format(moons_2.get_match_step())
