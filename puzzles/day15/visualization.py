import pygame
import numpy as np
import time
from random import randrange

from puzzle import read_input, get_verticies, ext_grid

# SETTINGS
SCREEN_X = 1000
SCREEN_Y = 1000
RESOLUTION = (SCREEN_X, SCREEN_Y)

pygame.init()
pygame.display.set_caption("where path")
display = pygame.display.set_mode(RESOLUTION)

MAIN_FONT = pygame.font.SysFont("Ubuntu", 50)

clock = pygame.time.Clock()

# COLORS
START = (0, 174, 255)
END   = (171, 31, 24)
BACKGROUND = (156, 156, 156)
LINE = (50, 50, 50)

class Rect():
    def __init__(self, GRID, START, END):
        self.GRID = GRID
        self.RECT_H = SCREEN_Y / GRID.shape[1]
        self.RECT_W = SCREEN_X / GRID.shape[0]
        self.START = START
        self.END = END

        self.RECTS = []
        for y in range(self.GRID.shape[1]):
            for x in range(self.GRID.shape[0]):
                y_loc = (SCREEN_Y / self.GRID.shape[1]) * y
                x_loc = (SCREEN_X / self.GRID.shape[0]) * x
                r = pygame.Rect(x_loc, y_loc, self.RECT_W, self.RECT_H)
                self.RECTS.append(r)
    
    def draw(self, y, x, c, w):
        r = self.RECTS[int(y*self.GRID.shape[1] + x)]
        pygame.draw.rect(display, c, r, w)
    
    def init_draw(self):
        for y in range(self.GRID.shape[1]):
            for x in range(self.GRID.shape[0]):
                c = (23, 92 + randrange(-10,10), 45)
                self.draw(y, x, c, 0)
                self.draw(y, x, LINE, 1)

    def update(self, v):
        self.draw(self.START[0], self.START[1], START, 0)
        for p in v:
            c = (34, 133 + randrange(-10,10), 66)
            self.draw(p[0], p[1], c, 0)
        self.draw(self.END[0], self.END[1], END, 0)
        
class Djikstra():
    def __init__(self, GRID, CLOCK, START, END):
        self.GRID = GRID
        self.START = START
        self.END = END
        self.STACK = [[0, [START]]]
        self.FOUND = set([START])
        self.CLOCK = CLOCK
        self.RECT  = Rect(GRID, START, END)

    def run(self):
        self.RECT.init_draw()

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            
            c = self.STACK[0][0]
            p = self.STACK[0][1]

            vs = get_verticies(self.GRID, p[-1][0], p[-1][1], self.FOUND)
            self.FOUND |= set(vs)

            if self.END in self.FOUND:
                s = 0
                for n in p:
                    s += self.GRID[n]
                    c = (0, randrange(150,220), randrange(174,255))
                    self.RECT.draw(n[0], n[1], c, 0)
                    pygame.display.update()
                    clock.tick(int(self.CLOCK/2))
                s += self.GRID[self.END]
                s -= self.GRID[self.START]
                
                rect = pygame.Surface((400,150), pygame.SRCALPHA, 32)
                rect.fill((34, 143, 66, 128))
                display.blit(rect, (SCREEN_X/2-200, SCREEN_Y/2-75))

                r = pygame.Rect(SCREEN_X/2-200, SCREEN_Y/2-75, 400, 150)
                pygame.draw.rect(display, (0,0,0), r, width=2)

                cost = MAIN_FONT.render(str(s), True, (0, 0, 0))
                cost_r = cost.get_rect(center=(SCREEN_X/2, SCREEN_Y/2))
                display.blit(cost, cost_r)
                pygame.display.update()
                time.sleep(5)
                exit()

            self.RECT.update(vs)
            pygame.display.update()

            del self.STACK[0]
            self.STACK += [[c+self.GRID[pr], p+[pr]] for pr in vs]
            self.STACK = sorted(self.STACK, key=lambda x: x[0])

            clock.tick(self.CLOCK)

def main():
    grid = np.array(read_input())
    grid = ext_grid(grid)

    start = (0,0)
    end   = tuple(np.subtract(grid.shape, (1,1)))
    prog = Djikstra(grid, 120, start, end)
    prog.run()

if __name__ == "__main__":
    main()