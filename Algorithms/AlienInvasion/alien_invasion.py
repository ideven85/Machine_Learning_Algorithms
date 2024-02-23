import sys
import pygame
class AlienVasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:

            for event in pygame.event.get():
                print(pygame.QUIT.real)
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
ai = AlienVasion()
ai.run_game()
