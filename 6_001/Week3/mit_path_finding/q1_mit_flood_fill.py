"""
Question 1: given the mit.png image, can we use the same flood_fill
function from the readings below to find all the buildings that are
connected to building 36? (run this file to find out!)

What if we wanted to know if we could reach a particular building
from 36?
"""


def flood_fill(image, location, new_color):
    """
    Given an image, replace the same-colored region around a given location
    with a given color.  Returns None but mutates the original image to
    reflect the change.

    Parameters:
      * image: the image to operate on
      * location: an (row, col) tuple representing the starting location of the
                  flood-fill process
      * new_color: the replacement color, as an (r, g, b) tuple where all values
                   are between 0 and 255, inclusive
    """
    print(f"You clicked at row {location[0]} col {location[1]}")
    original_color = get_pixel(image, *location)

    def get_neighbors(cell):
        row, col = cell
        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        return [
            (r, c)
            for (r, c) in neighbors
            if 0 <= r < get_height(image) and 0 <= c < get_width(image)
        ]

    def close(color1, color2):
        return sum(abs(c1 - c2) for c1, c2 in zip(color1, color2)) <= 25

    to_color = [location]
    visited = {location}
    # print("before loop")
    while to_color:
        this_cell = to_color.pop(0)
        set_pixel(image, *this_cell, new_color)
        for neighbor in get_neighbors(this_cell):
            if neighbor not in visited and close(
                get_pixel(image, *neighbor), original_color
            ):
                to_color.append(neighbor)
                visited.add(neighbor)
    # print("after loop")


def find_path(image, start_location, goal_color):
    """
    Given an image, replace the same-colored region around a given location
    with a given color.  Returns None but mutates the original image to
    reflect the change.

    Parameters:
      * image: the image to operate on
      * location: an (row, col) tuple representing the starting location of the
                  flood-fill process
      * new_color: the replacement color, as an (r, g, b) tuple where all values
                   are between 0 and 255, inclusive
    """

    path_color = get_pixel(image, *start_location)
    print(
        f"You clicked at row {start_location[0]} col {start_location[1]}, {path_color}"
    )

    def get_neighbors(cell):
        row, col = cell
        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        return [
            (r, c)
            for (r, c) in neighbors
            if 0 <= r < get_height(image) and 0 <= c < get_width(image)
        ]

    paths = [(start_location,)]
    visited = {start_location}
    # print("before loop")
    final_path = None
    while paths:
        this_path = paths.pop(0)
        if get_pixel(image, *this_path[-1]) == goal_color:
            print("found!", this_path)
            final_path = this_path
            break  # found solution

        for neighbor in get_neighbors(this_path[-1]):
            if neighbor not in visited and get_pixel(image, *neighbor) in {
                path_color,
                goal_color,
            }:
                paths.append(this_path + (neighbor,))
                # print(paths[-1])
                visited.add(neighbor)
    print(len(paths))
    if final_path:
        print(len(final_path))
        for cell in final_path:
            set_pixel(image, *cell, goal_color)
        print(*final_path[-1])
    else:
        print("No path found, explored", len(visited))


##### IMAGE REPRESENTATION WITH SIMILAR ABSTRACTIONS TO LAB 1 AND 2


def get_width(image):
    return image.get_width() // SCALE


def get_height(image):
    return image.get_height() // SCALE


def get_pixel(image, row, col):
    color = image.get_at((col * SCALE, row * SCALE))
    return (color.r, color.g, color.b)


def set_pixel(image, row, col, color):
    loc = row * SCALE, col * SCALE
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

SCALE = 1  # 7
IMAGE = "huge_maze.png"

pygame.init()
image = pygame.image.load(IMAGE)
dims = (image.get_width() * SCALE, image.get_height() * SCALE)
screen = pygame.display.set_mode(dims)
image = pygame.transform.scale(image, dims)
screen.blit(image, (0, 0))
pygame.display.flip()
initial_color = pygame.K_p
cur_color = COLORS[initial_color]
print("current color:", COLOR_NAMES[initial_color])
goal_color = (0, 255, 0)

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
            find_path(image, (event.pos[1] // SCALE, event.pos[0] // SCALE), cur_color)
            screen.blit(image, (0, 0))
            pygame.display.flip()
