import random, sys
from game_utils import *


class GamePiece:
    """
    A piece in the ETS game. Each GamePiece has the following attributes:
    * symbol (str) - single char representation
    * color (str) - color of the symbol (ie. red, white)
    * position - (row, col) integer tuple

    All game objects update every timestep, and render their current state at
    the end of every timestep.
    """

    symbol = "?"
    color = "white"
    alive = True

    def __init__(self, position):
        self.position = position

    def update(self, game):
        """
        Given the current game state, update the object.
        """
        pass

    def render(self):
        """
        Takes the state of the object at the end of a timestep and displays
        it to the screen.
        """
        print_at_location(*self.position, self.symbol, self.color)


class Wall(GamePiece):
    pass


class Sock(GamePiece):
    pass


# Implement sock and wall first, then add in players!
class Player(GamePiece):
    """
    A movable game piece represented by the "@" symbol. Each player has a score
    that increases when they intersect with a sock. Players move in their
    current set direction once every "steps_between_moves" game steps.
    """

    symbol = "@"

    def __init__(self, position):
        GamePiece.__init__(self, position)
        self.direction = None
        self.score = 0

    def update(self, game):
        delta = game.movement_deltas[self.direction]
        new_position = tuple(i + j for i, j in zip(self.position, delta))
        if not game.objects_at(new_position, Wall):
            # move if we won't land on a wall
            self.position = new_position

        # check for socks that we're intersecting, gain points
        socks_here = game.objects_at(self.position, Sock)
        for sock in socks_here:
            self.score += sock.value
            sock.alive = False


class Bot(Player):
    pass


class Human(Player):
    pass


class Game:
    """
    Creates a game of the given dimensions surrounded by walls and two players
    in opposite corners.

    Runs the game for the given duration, randomly generating socks and moving
    players around each time step. Renders the updated board by printing it
    to the terminal at the end of every timestep.

    Declares winner at the end.
    """

    step_rate = 10  # game updates 10 times per second
    # constants used for movement / changing direction
    directions = "UP", "DOWN", "LEFT", "RIGHT"
    UP, DOWN, LEFT, RIGHT, NO_DIRECTION = *directions, None
    opposite_keys = {
        UP: DOWN,
        LEFT: RIGHT,
        RIGHT: LEFT,
        DOWN: UP,
        None: None,
    }

    movement_deltas = {
        UP: (-1, 0),
        DOWN: (1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1),
        None: (0, 0),
    }

    def __init__(self, height, width, duration=15):
        """
        height (int) num rows
        width (int)  num columns
        duration (int) number of seconds in the game
        """
        self.height = height
        self.width = width
        self.time_steps = duration * self.step_rate
        self.steps_remaining = self.time_steps
        # make players in opposite corners
        self.player = Human((height - 1, 2))  # bottom-left (h-1, 2)
        self.bot = Bot((2, width - 1))  # top-right (2, w-1)
        self.all_pieces = [self.player, self.bot]
        # add players and walls to all_pieces
        # make walls left (r, 1) right (r, w)
        for r in range(1, width + 1):
            self.all_pieces.append(Wall((r, 1)))
            self.all_pieces.append(Wall((r, width)))
        # make walls top (1, c), bottom (h, c)
        for c in range(1, height + 1):
            self.all_pieces.append(Wall((1, c)))
            self.all_pieces.append(Wall((height, c)))

    def run(self):
        with keystrokes(sys.stdin) as keyb:
            for i in range(self.time_steps):
                self.steps_remaining -= 1
                self.keys = keyb.regioned_keys()
                self.update()
                self.render()
                time.sleep(1 / self.step_rate)  # pause between each game step

        # TODO after the game is over, display the winner
        text = "GAME OVER"
        color = "red"
        print_at_location(5, self.width + 2, text, color)

    def update(self):
        # randomly decide whether to add a sock
        if random.random() < 0.2:
            # generate a random position in bounds
            r = random.randint(2, self.height - 1)
            c = random.randint(2, self.width - 1)
            self.all_pieces.append(Sock((r, c)))

        # update positions of all the objects
        for piece in self.all_pieces:
            piece.update(self)

        # TODO remove socks that have disappeared

    def render(self):
        clear_screen()  # make new screen
        # print remaining time below the board
        text = "Time: " + str(self.steps_remaining)
        print_at_location(1, self.width + 2, text, "white")
        print_at_location(3, self.width + 2, f"You: {self.player.score}", "white")
        print_at_location(4, self.width + 2, f"Bot: {self.player.score}", "white")

        # display the objects on the board
        for piece in self.all_pieces:
            piece.render()

    def objects_at(self, position, instance_of=object):
        return [
            thing
            for thing in self.all_pieces
            if thing.position == position and isinstance(thing, instance_of)
        ]


if __name__ == "__main__":
    # create and run a 20 by 20 game that runs for 5 seconds
    game = Game(20, 20, 5)
    game.run()
