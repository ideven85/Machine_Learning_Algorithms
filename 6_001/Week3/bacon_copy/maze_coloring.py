import pygame
import os
import sys

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
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
IMAGE = "large_maze.png"

pygame.init()
pygame.display.set_caption("Shortest Path Finder")


def flood_fill(maze_image, starting_location, new_color):
    print("You clicked at ", *starting_location)
    original_color = get_pixel(maze_image, *starting_location)
    current = [starting_location]
    visited = {starting_location}
    while current:
        to_color = current.pop(0)
        set_pixel(maze_image, *to_color, new_color)
        neighbours = get_neighbors(to_color)
        for neighbour in neighbours:
            if (
                neighbour not in visited
                and get_pixel(maze_image, *neighbour) == original_color
            ):
                current.append(neighbour)
                visited.add(neighbour)


def shortest_path_finder(maze_image, starting_location, goal_color):
    """
    In the image of the maze
    Given a starting position, find the shortest path to the goal_color
    """
    print("You clicked at ", *starting_location)
    original_color = get_pixel(maze_image, *starting_location)
    # set_pixel(maze_image,*starting_location,goal_color)
    # if get_pixel(image, *this_path[-1]) == goal_color:
    # def get_neighbours(row,col):
    #     neighbours = [(row-1,col),(row+1,col),(row,col-1),(row,col+1) ]
    #     return [(r,c)
    #             for (r,c) in neighbours
    #             if 0<=get_height(maze_image)<r
    #             and 0<=get_width(maze_image)<c]
    # paths = [starting_location]
    # visited = {starting_location}
    # final_path = None
    # current_path = []
    # while paths:
    #     current = paths.pop(0)
    #     current_path.append(current)
    #     if get_pixel(maze_image,*current)==goal_color:
    #         print("Path Found")
    #         final_path=current_path
    #         break
    #     connections = get_neighbours(*current)
    #     for conn in connections:
    #         if conn in visited:
    #             continue
    #         visited.add(conn)
    #         current.append(conn)
    # if not final_path:
    #     print("No path found",len(visited))
    #     return
    # for path in final_path:
    #     set_pixel(maze_image,*path,goal_color)
    # print("Total Paths Explored:", len(visited))
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

    path_color = get_pixel(image, *starting_location)
    print(
        f"You clicked at row {starting_location[0]} col {starting_location[1]}, {path_color}"
    )

    paths = [(starting_location,)]
    visited = {starting_location}
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
    else:
        print("No path found, explored", len(visited))


def get_neighbors(cell):
    row, col = cell
    neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    return [
        (r, c)
        for (r, c) in neighbors
        if 0 <= r < get_height(image) and 0 <= c < get_width(image)
    ]


def get_height(maze_image):
    return maze_image.get_height() // SCALE


def get_width(maze_image):
    return maze_image.get_width() // SCALE


def get_pixel(maze_image, row, col):
    return maze_image.get_at((row * SCALE, col * SCALE))


def set_pixel(maze_image, row, col, color):
    location = row * SCALE, col * SCALE
    c = pygame.Color(*color)
    for i in range(SCALE):
        for j in range(SCALE):
            maze_image.set_at((location[1] + i, location[0] + j), c)
    screen.blit(maze_image, (0, 0))
    pygame.display.flip()


image = pygame.image.load(IMAGE)
dims = (image.get_width() * SCALE, image.get_height() * SCALE)
screen = pygame.display.set_mode(dims)
image = pygame.transform.scale(image, dims)
screen.blit(image, (0, 0))
pygame.display.flip()
initial_color = pygame.K_p
current_color = COLORS[initial_color]
print("current color:", COLOR_NAMES[initial_color])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key in COLORS:
                current_color = COLORS[event.key]
                print("current color:", COLOR_NAMES[event.key])
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flood_fill(
                image, (event.pos[1] // SCALE, event.pos[0] // SCALE), current_color
            )

            # shortest_path_finder(image, (event.pos[1] // SCALE, event.pos[0] // SCALE), current_color)
            screen.blit(image, (0, 0))
            pygame.display.flip()
