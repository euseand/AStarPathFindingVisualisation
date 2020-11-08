import pygame
import math
import constants
import utils

from queue import PriorityQueue
from spot import Spot



def main_loop():
    window = pygame.display.set_mode((constants.WIDTH,constants.WIDTH))
    pygame.display.set_caption('A* Algorithm Visualisation') 

    rows = 50
    width = constants.WIDTH

    grid = utils.make_grid(rows, width)

    start_spot = None
    end_spot = None

    run_loop = True
    search_started = False

    while run_loop:
        utils.draw(window, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_loop = False

            if search_started:
                continue

            if pygame.mouse.get_pressed()[0]: #LEFT MOUSE BUTTON
                pos = pygame.mouse.get_pos()
                row, col = utils.get_click_pos(pos, rows, width)
                spot = grid[row][col]
                if not start_spot and spot != end_spot:
                    start_spot = spot
                    start_spot.make_start()

                elif not end_spot and spot != start_spot:
                    end_spot = spot
                    end_spot.make_end()
                
                elif spot != start_spot and spot != end_spot:
                    spot.make_wall()

            elif pygame.mouse.get_pressed()[2]: #RIGHT MOUSE BUTTON
                pos = pygame.mouse.get_pos()
                row, col = utils.get_click_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start_spot:
                    start_spot = None
                elif spot == end_spot:
                    end_spot = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not search_started:
                    pass

    pygame.quit()

if __name__ == '__main__':
    main_loop()