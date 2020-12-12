
import common

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


class Seat(object):
    def __init__(self, x, y, seat):
        self.x = x
        self.y = y
        self.seat = seat
        self.tmp_seat = seat

    def get_adjacent_seats(self, grid, use_seen=False):
        indexes = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1),
                   (1, 1), (-1, 1))
        seats = []

        for _x, _y in indexes:
            x = self.x + _x
            y = self.y + _y
            has_complete = False

            while not has_complete:
                if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]):
                    item = grid[x][y]

                    if not use_seen or (use_seen and item.seat != FLOOR):
                        seats.append(item)
                        has_complete = True
                    else:
                        x += _x
                        y += _y
                else:
                    break

        return [seat.seat for seat in seats]


class SeatingPlan(object):
    def __init__(self, seats, grid):
        self.seats = seats
        self.grid = grid

    @classmethod
    def from_data(cls, data):
        grid = []
        all_seats = []

        for x, row in enumerate(data):
            seats = []

            for y, seat in enumerate(row):
                seat = Seat(x, y, seat)

                seats.append(seat)
                all_seats.append(seat)

            grid.append(seats)

        return cls(all_seats, grid)

    def set_seats(self):
        for item in self.seats:
            if item.seat == item.tmp_seat:
                continue

            item.seat = item.tmp_seat

    def get_adjacent_plan(self, num=4, use_seen=False):
        has_complete = False

        while not has_complete:
            for index, item in enumerate(self.seats):
                if item.seat == FLOOR:
                    continue

                adjacent_seats = item.get_adjacent_seats(self.grid, use_seen)
                total_occupied = adjacent_seats.count(OCCUPIED)

                if item.seat == EMPTY and total_occupied == 0:
                    item.tmp_seat = OCCUPIED
                elif item.seat == OCCUPIED and total_occupied >= num:
                    item.tmp_seat = EMPTY

            has_complete = not any(x.seat != x.tmp_seat for x in self.seats)
            self.set_seats()

        return [item.seat for item in self.seats].count(OCCUPIED)


data = common.get_lines(__file__)
plan_1 = SeatingPlan.from_data(data)
plan_2 = SeatingPlan.from_data(data)

print('Part 1: {}'.format(plan_1.get_adjacent_plan()))
print('Part 2: {}'.format(plan_2.get_adjacent_plan(num=5, use_seen=True)))
