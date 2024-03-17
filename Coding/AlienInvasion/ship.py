import pygame

class Ship:

    def __init__(self, ai_game):
        # Where is the call to super constructor()?

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.moving_right=False
        self.moving_left=False

    def repaint(self):
        self.screen.blit(self.image, self.rect)
        if self.moving_right:
            self.rect.x +=1
        if self.moving_left:
            self.rect.x -=1
