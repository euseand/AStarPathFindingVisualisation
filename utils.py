import constants
import pygame

from spot import Spot

def heuristic_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, constants.GREY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, constants.GREY, (j*gap, 0), (j*gap, width))

def draw(window, grid, rows, width):
    window.fill(constants.WHITE)    
    for row in grid:
        for spot in row:
            spot.draw(window)    
    draw_grid(window, rows, width)
    pygame.display.update()

def get_click_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col