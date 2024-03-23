import collections
import time

count = 0




def get_neighbours(cell):
    row, col = cell
    potential_neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [(nr, nc) for (nr, nc) in potential_neighbours if 0 <= nr < get_height(image) and 0 <= nc < get_width(image)]


def flood_fill(image, original_location, new_color):
    original_color = get_pixel(image, *original_location)
    #visited = {original_location}
    print(f"You clicked at row {original_location[0]} col {original_location[1]}")
    if original_color == new_color:
        return

    start = time.time()

    def fill_from(location):

        global count
        count += 1
        set_pixel(image, *location, new_color)
        for neighbor in get_neighbours(location):
            if  get_pixel(image, *neighbor) == original_color:
                #visited.add(neighbor)
                fill_from(neighbor)

    fill_from(original_location)

    print("Time taken:", time.time() - start)


def get_width(image):
    return image.get_width() // SCALE


def get_height(image):
    return image.get_height() // SCALE


def get_pixel(image, row, col):
    color = image.get_at((col * SCALE, row * SCALE))
    return (color.r, color.g, color.b)


def set_pixel(image, row, col, color):
    loc = row * SCALE, col * SCALE
    # if get_width(image)>col or get_height(image)>row:
    #     return

    c = pygame.Color(*color)
    for i in range(SCALE):
        for j in range(SCALE):
            image.set_at((loc[1] + i, loc[0] + j), c)
    ## comment out the two lines below to avoid redrawing the image every time
    ## we set a pixel
    screen.blit(image, (0, 0))
    pygame.display.flip()


##### USER INTERFACE CODE
##### DISPLAY AN IMAGE AND CALL flood_fill WHEN THE IMAGE IS CLICKED

import os
import sys

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from pygame.locals import *

COLORS = {
    pygame.K_r: (255, 0, 0),
    pygame.K_w: (255, 255, 255),
    pygame.K_k: (0, 0, 0),
    pygame.K_g: (0, 255, 0),
    pygame.K_b: (0, 0, 255),
    pygame.K_c: (0, 255, 255),
    pygame.K_y: (255, 230, 0),
    pygame.K_p: (179, 0, 199),
    pygame.K_o: (255, 77, 0),
    pygame.K_n: (66, 52, 0),
    pygame.K_e: (152, 152, 152),
}

COLOR_NAMES = {
    pygame.K_r: "red",
    pygame.K_w: "white",
    pygame.K_k: "black",
    pygame.K_g: "green",
    pygame.K_b: "blue",
    pygame.K_c: "cyan",
    pygame.K_y: "yellow",
    pygame.K_p: "purple",
    pygame.K_o: "orange",
    pygame.K_n: "brown",
    pygame.K_e: "grey",
}

SCALE = 7
IMAGE = "flood_input.png"

pygame.init()
pygame.display.set_caption("Flood Fill DFS")
image = pygame.image.load(IMAGE)
dims = (image.get_width() * SCALE, image.get_height() * SCALE)
screen = pygame.display.set_mode(dims)
image = pygame.transform.scale(image, dims)
screen.blit(image, (0, 0))
pygame.display.flip()
initial_color = pygame.K_p
cur_color = COLORS[initial_color]
print("current color:", COLOR_NAMES[initial_color])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key in COLORS:
                cur_color = COLORS[event.key]
                print("current color:", COLOR_NAMES[event.key])
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            flood_fill(image, (event.pos[1] // SCALE, event.pos[0] // SCALE), cur_color)
            print(count)
            # print((end - start) * 10)

            screen.blit(image, (0, 0))
            pygame.display.flip()
# Time taken: 0.9041509628295898
# Time taken: 0.8100771903991699
# Time taken: 0.7933170795440674

# You clicked at row 63 col 40
# Time taken: 0.8618607521057129