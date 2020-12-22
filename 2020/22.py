
import common


class Combat(object):
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    @classmethod
    def from_data(cls, data):
        player_1 = [int(item) for item in data[0].split('\n')[1:]]
        player_2 = [int(item) for item in data[1].split('\n')[1:]]

        return cls(player_1, player_2)

    def run(self):
        total = len(self.player_1) + len(self.player_2)

        while len(self.player_1) != total and len(self.player_2) != total:
            player_1_card = self.player_1[0]
            player_2_card = self.player_2[0]

            self.player_1 = self.player_1[1:]
            self.player_2 = self.player_2[1:]

            if player_1_card > player_2_card:
                self.player_1.append(player_1_card)
                self.player_1.append(player_2_card)
            else:
                self.player_2.append(player_2_card)
                self.player_2.append(player_1_card)

        cards = self.player_2 if len(self.player_1) == 0 else self.player_1
        cards.reverse()

        return sum([item * (index + 1) for index, item in enumerate(cards)])


data = common.get_lines(__file__, split='\n\n')
game = Combat.from_data(data)

print('Part 1: {}'.format(game.run()))
