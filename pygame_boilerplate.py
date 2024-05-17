import sys

import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Boilerplate")

# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(0)

    # Update the game state

    # Draw everything
    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
