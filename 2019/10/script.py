
from math import atan2, degrees, sqrt


class Asteroid(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_angles(self, asteroids):
        data = []

        for asteroid in asteroids:
            if self == asteroid:
                continue

            data.append(atan2(asteroid.y - self.y, asteroid.x - self.x))

        return data

    def get_visible(self, asteroids):
        return len(set(self.get_angles(asteroids)))

    def get_distance(self, station):
        return sqrt((self.x - station.x) ** 2 + (self.y - station.y) ** 2)


class Asteroids(object):
    LASER_DEGREE = 90

    def __init__(self, asteroids, station):
        self.asteroids = asteroids
        self.station = station

    @classmethod
    def from_data(cls):
        text = open('input.txt').read()
        asteroids = []
        station = None

        for y, item in enumerate(text.split('\n')):
            for x, character in enumerate(item):
                if character == '.':
                    continue

                asteroids.append(Asteroid(x, y))

        return cls(asteroids, station)

    def get_most_visible(self):
        data = [[x.get_visible(self.asteroids), x] for x in self.asteroids]
        data.sort()
        self.station = data[-1][1]
        self.asteroids.remove(self.station)
        return data[-1][0]

    def get_blank_angles(self):
        data = {}

        for item in self.asteroids:
            angle = item.get_angles([self.station])[0]
            angle = degrees(angle) % 360
            angle = angle if angle >= self.LASER_DEGREE else angle + 360

            if angle not in data:
                data[angle] = []

            data[angle].append([item.get_distance(self.station), item])

        return data

    def vapourise(self):
        vapourised = []
        data = self.get_blank_angles()
        sorted_keys = data.keys()
        sorted_keys.sort()

        while len(vapourised) != len(self.asteroids):
            for item in sorted_keys:
                if len(data[item]) == 0:
                    continue

                data[item].sort()
                vapourised.append(data[item][0][1])
                del data[item][0]

        return vapourised


asteroids = Asteroids.from_data()
most_visible = asteroids.get_most_visible()
vapourised = asteroids.vapourise()

print 'Part 1: {}'.format(most_visible)
print 'Part 2: {}'.format(vapourised[199].x * 100 + vapourised[199].y)
