import sys
import pygame

from settings import Settings
from ship import Ship

#todo Add more Logic
class AlienVasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        #self.bg_color = (230, 230, 230)
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:

            self._action_listener()
            self._repaint()

            self.clock.tick(120)
    def _action_listener(self):
        for event in pygame.event.get():
            #print(pygame.QUIT.real)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _repaint(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.repaint()
        pygame.display.flip()

ai = AlienVasion()
ai.run_game()
