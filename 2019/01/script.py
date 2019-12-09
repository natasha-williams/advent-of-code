
from math import floor


def get_fuel(mass):
    return int(floor(mass / 3) - 2)


def get_added_fuel(fuel):
    total = 0

    while fuel > 0:
        total += fuel
        fuel = get_fuel(fuel)

    return total


def get_lines():
    text = open('input.txt').read()
    return [item for item in text.split('\n')]


total_fuel = 0
total_added_fuel = 0

for item in get_lines():
    number = int(item)
    fuel = get_fuel(number)

    total_fuel += fuel
    total_added_fuel += get_added_fuel(fuel)

print('Part 1: {}'.format(total_fuel))
print('Part 2: {}'.format(total_added_fuel))
