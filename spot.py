import constants as const
from pygame.draw import rect as draw_rect

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col        
        self.width = width
        self.total_rows = total_rows
        self.x = row*width
        self.y = col*width
        self.color = const.WHITE
        self.neighbours = []

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == const.RED

    def is_open(self):
        return self.color == const.GREEN
    
    def is_wall(self):
        return self.color == const.BLACK

    def is_start(self):
        return self.color == const.ORANGE

    def is_end(self):
        return self.color == const.AZURE

    def reset(self):
        self.color = const.WHITE

    def make_closed(self):
        self.color = const.RED

    def make_open(self):
        self.color = const.GREEN
    
    def make_wall(self):
        self.color = const.BLACK

    def make_start(self):
        self.color = const.ORANGE

    def make_end(self):
        self.color = const.AZURE

    def make_path(self):
        self.color = const.PURPLE

    def draw(self, window):
        draw_rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False