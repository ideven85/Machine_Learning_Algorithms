import pygame

# Main Entry for pygame


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pong")

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()

        # Quit game
        pygame.quit()


if __name__ == "__main__":
    main = Main()
