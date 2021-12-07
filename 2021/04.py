
import copy

import utils


class Bingo(object):
    def __init__(self, boards, numbers, total):
        self.boards = boards
        self.numbers = numbers
        self.total = total

    @classmethod
    def from_data(cls):
        data = utils.get_data(__file__, split_at='\n\n')
        numbers = [int(x) for x in data[0].split(',')]
        boards = []

        for item in data[1:]:
            board = [[int(y) for y in x.split()] for x in item.split('\n')]
            boards.append((board, list(map(list, zip(*board)))))

        return cls(boards, numbers, len(data[1:]))

    def is_winner(self, board):
        return len(list(filter(None, board))) == len(board) - 1

    def play(self, play_to_lose=False):
        boards = copy.deepcopy(self.boards)
        winning_boards = []
        winning_scores = []

        for number in self.numbers:
            if len(winning_boards) == self.total:
                break

            for board_index, board in enumerate(boards):
                for board_type_index, board_type in enumerate(board):
                    for line_index, line in enumerate(board_type):
                        if number in line:
                            boards[board_index][board_type_index][line_index].remove(number)

                    if self.is_winner(boards[board_index][board_type_index]) and board_index not in winning_boards:
                        score = sum([sum(x) for x in boards[board_index][board_type_index]])
                        winning_scores.append(number * score)
                        winning_boards.append(board_index)

        return winning_scores[-1] if play_to_lose else winning_scores[0]


bingo = Bingo.from_data()
print('Part 1: {}'.format(bingo.play()))
print('Part 2: {}'.format(bingo.play(play_to_lose=True)))
