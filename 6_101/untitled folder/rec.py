# 6.101 recitation: Eat That Sock

import random, sys
from game_utils import *


class GameItem:
    color = "white"
    alive = True

    def __init__(self, position):
        self.position = position

    def update(self, game):
        pass

    def render(self):
        print_at_location(*self.position, self.symbol, self.color)


class Wall(GameItem):
    symbol = "#"

    # def __init__(self, position):
    #    GameItem.__init__(self, position, '#', 'white')


class Sock(GameItem):
    color_points = {"blue": 3, "green": 2, "red": 1}
    symbol = "s"

    def __init__(self, position, color, ttl):
        GameItem.__init__(self, position)
        self.color = color
        self.ttl = ttl

    def update(self, game):
        if self.ttl == 0:
            self.alive = False
        else:
            self.ttl -= 1

    @property
    def value(self):
        return self.color_points[self.color]


class MobileGameItem(GameItem):
    movement_deltas = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1),
        None: (0, 0),
    }
    opposites = {
        "UP": "DOWN",
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
        "DOWN": "UP",
        None: None,
    }

    def __init__(self, position, time_between_moves):
        GameItem.__init__(self, position)
        self.time_between_moves = time_between_moves
        self.direction = None

    def update(self, game):
        if game.round_number % self.time_between_moves == 0:
            delta = self.movement_deltas[self.direction]
            new_position = tuple(i + j for i, j in zip(self.position, delta))

            if not game.items_at(new_position, Wall):
                self.position = new_position


class Player(MobileGameItem):
    symbol = "@"

    def __init__(self, position, time_between_moves):
        self.score = 0
        MobileGameItem.__init__(self, position, time_between_moves)

    def update(self, game):
        MobileGameItem.update(self, game)

        for sock in game.items_at(self.position, Sock):
            sock.alive = False
            self.score += sock.value


class Human(Player):
    def update(self, game):
        self.color = random.choice(list(color_map.keys()))

        for region, key in game.keys:
            if key in self.movement_deltas:
                if key == self.opposites[self.direction]:
                    self.direction = None
                else:
                    self.direction = key
        Player.update(self, game)


class Bot(Player):
    color = "magenta"

    def update(self, game):
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        Player.update(self, game)


fps = 10


class Game:
    def __init__(self, height, width, duration=20 * 30):
        self.height = height
        self.width = width
        self.duration = duration

        self.all_items = []
        for r in range(1, height + 1):
            self.all_items.append(Wall((r, 1)))
            self.all_items.append(Wall((r, width)))
        for c in range(2, width):
            self.all_items.append(Wall((1, c)))
            self.all_items.append(Wall((height, c)))

        self.player = Human((height - 1, 2), 1)
        self.bot = Bot((2, width - 1), 1)

        self.all_items.append(self.player)
        self.all_items.append(self.bot)

    def items_at(self, position, instance_of=object):
        return [
            thing
            for thing in self.all_items
            if thing.position == position and isinstance(thing, instance_of)
        ]

    def _maybe_add_sock(self):
        if random.random() < 0.2:
            r = random.randint(2, self.height - 1)
            c = random.randint(2, self.width - 1)
            color = random.choice(["red", "green", "blue"])
            ttl = random.randint(5, 50)
            self.all_items.append(Sock((r, c), color, ttl))

    def update(self):
        self._maybe_add_sock()

        for e in self.all_items:
            e.update(self)

        self.all_items = [e for e in self.all_items if e.alive]

    def render(self):
        clear_screen()
        print_at_location(self.height + 1, 0, "You: " + str(self.player.score))
        print_at_location(self.height + 2, 0, "Bot: " + str(self.bot.score))
        print_at_location(
            self.height + 3, 0, "Time: " + str(self.duration - self.round_number)
        )
        for e in self.all_items:
            e.render()

    def run(self):
        with keystrokes(sys.stdin) as keyb:
            for i in range(self.duration):
                self.round_number = i
                self.keys = keyb.regioned_keys()
                self.update()
                self.render()
                time.sleep(1 / fps)

        if self.player.score > self.bot.score:
            text = "A WINNER IS YOU!"
            color = "green"
        else:
            text = "LOST :("
            color = "red"
        print_at_location(self.height + 4, 0, text, color)

        input("Press Enter to continue")


if __name__ == "__main__":
    Game(20, 20, 30 * fps).run()
