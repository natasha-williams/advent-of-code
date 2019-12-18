
import path

from intcode import LoopIntcodeGenerator


class Game(object):
    FREE_PLAY_MODE = 2
    PADDLE_ID = 3
    BALL_ID = 4

    def __init__(self, generator, is_free_play):
        self.generator = generator
        self.is_free_play = is_free_play
        self.paddle = (0, 0, 0)
        self.ball = (0, 0, 0)
        self.score = 0

    @classmethod
    def from_generator(cls, is_free_play=False):
        generator = LoopIntcodeGenerator.from_data()

        if is_free_play:
            generator.data[0] = cls.FREE_PLAY_MODE

        return cls(generator, is_free_play)

    def play(self):
        data = []

        while not self.generator.has_complete:
            mode = self.get_mode()
            x = self.generator.run(mode)
            y = self.generator.run(mode)
            tile_id = self.generator.run(mode)

            if x == -1 and y == 0:
                self.score = tile_id
            elif self.is_free_play and tile_id == self.PADDLE_ID:
                self.paddle = [x, y, tile_id]
            elif self.is_free_play and tile_id == self.BALL_ID:
                self.ball = [x, y, tile_id]

            data.append([x, y, tile_id])

        return data

    def count(self, tile=2):
        return [item[-1] for item in self.play()].count(tile)

    def get_score(self):
        self.play()
        return self.score

    def get_mode(self):
        mode = -1 if self.paddle[0] > self.ball[0] else 1
        return 0 if self.paddle[0] == self.ball[0] else mode


game_1 = Game.from_generator()
game_2 = Game.from_generator(is_free_play=True)

print 'Part 1: {}'.format(game_1.count())
print 'Part 2: {}'.format(game_2.get_score())
