import pygame
import sys
pygame.init()
HEIGHT = 1280
WIDTH = 720
SCREEN = ( WIDTH,HEIGHT)
screen = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width()//2, screen.get_height()//2)


def isvalid(player_position):
    print(player_position[0], player_position[1])
    return True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
                running=False
        screen.fill("purple")
        pygame.draw.circle(screen, "red",player_pos,40)
        keys = pygame.key.get_pressed()
        print(player_pos)
        if isvalid(player_pos):
            if keys[pygame.K_w]:
                player_pos.y -=300*dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * dt
        pygame.display.flip()
        dt=clock.tick(0)/1000

pygame.quit()
