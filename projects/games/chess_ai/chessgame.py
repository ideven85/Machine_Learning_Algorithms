# Learning Pygame, making a chess engine
#
# Can do in Django if pygame not possible...
import pygame
import sys
#todo make chessai
pygame.init()


def exit_game():
    if event.type == pygame.QUIT:
        return True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            return True
    return False


screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))
x_pos = 600
y_pos = 500
while True:

    for event in pygame.event.get():
        if exit_game():
            pygame.quit()
            sys.exit(1)

    screen.fill((175, 210, 30))
    # x_pos+=1
    y_pos -= 1
    screen.blit(test_surface, (x_pos, y_pos))
    pygame.display.update()
    clock.tick(60)
