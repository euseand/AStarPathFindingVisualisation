import pygame
import math
import utils


from spot import Spot
from constants import WIDTH


def main_loop():
    window = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('A* Pathfinding Algorithm Visualisation')

    rows = 50
    width = WIDTH

    grid = utils.make_grid(rows, width)

    start_spot = None
    end_spot = None

    run_loop = True

    while run_loop:        
        utils.draw(window, grid, rows, width)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_loop = False

            if pygame.mouse.get_pressed()[0]: #left mouse button = draw
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

            elif pygame.mouse.get_pressed()[2]: #right mouse button - erase
                pos = pygame.mouse.get_pos()
                row, col = utils.get_click_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start_spot:
                    start_spot = None

                elif spot == end_spot:
                    end_spot = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_spot and end_spot:
                    for row in grid:                        
                        for spot in row:
                            spot.update_neighbors(grid)
                        
                    utils.pathfinding_algorithm(lambda: utils.draw(window, grid, rows, width), grid, start_spot, end_spot)

                if event.key == pygame.K_c:
                    start_spot = None
                    end_spot = None
                    grid = utils.make_grid(rows, width)

    pygame.quit()

if __name__ == '__main__':
    main_loop()