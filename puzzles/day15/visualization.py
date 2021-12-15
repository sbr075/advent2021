"""
Written fast just to see how the puzzle looks like visually
"""

import pygame
import numpy as np
from puzzle import read_input, get_verticies
import time

MAIN_TEXT  = (32, 170, 24)

LOCKED     = (32, 50, 24)
UNLOCKED   = (32, 130, 24)
SEARCHING  = (32, 220, 24)

BACKGROUND = (10, 30, 55)

START = (24, 97, 171)
END   = (171, 31, 24)

SCREEN_X = 800
SCREEN_Y = 800
RESOLUTION = (SCREEN_X, SCREEN_Y)

pygame.init()
pygame.display.set_caption("where path")
display = pygame.display.set_mode(RESOLUTION)

MAIN_FONT = pygame.font.SysFont("consolas", 20, bold=True)

CLOCK = 5

clock = pygame.time.Clock()
def main():
    grid = np.array(read_input())
    e = tuple(np.subtract(grid.shape, (1,1)))

    stack = [[0, [(0,0)]]]
    v = set([(0,0)])
    searched = []

    display.fill(BACKGROUND)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        
        c = stack[0][0]
        p = stack[0][1]
        searched.append(p[-1])

        if p[-1] == e:
            shortest_txt = MAIN_FONT.render(f"Shortest path: {stack[0][0]}", True, MAIN_TEXT)
            display.blit(shortest_txt, (30, 30))

            for p in stack[0][1]:
                y = p[1]
                x = p[0]
                r = pygame.Rect(40+((SCREEN_Y - 20) / 10)*y, 80+((SCREEN_X - 60) / 10)*x, 20, 20)
                pygame.draw.rect(display, START, r)
                pygame.display.update()
                clock.tick(CLOCK)

            time.sleep(5)
            break
        
        vs = get_verticies(grid, p[-1][0], p[-1][1], v)
        v|=set(vs)

        del stack[0]
        stack += [[c+grid[pr], p+[pr]] for pr in vs]

        stack = sorted(stack, key=lambda x: x[0])

        rects = []
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                r = pygame.Rect(40+((SCREEN_Y - 20) / 10)*y, 80+((SCREEN_X - 60) / 10)*x, 20, 20)
                if (y,x) == (0,0):
                    color = START
                elif (y,x) == e:
                    color = END
                elif (y,x) == p[-1]:
                    color = SEARCHING
                elif (y,x) in searched:
                    color = UNLOCKED
                else:
                    color = LOCKED
                rects.append([color, r])
        
        display.fill(BACKGROUND, rect=(0,0, SCREEN_X, 70))
        searched_txt = MAIN_FONT.render(f"Searched: {len(searched)}", True, MAIN_TEXT)
        display.blit(searched_txt, (30, 10))

        for rect in rects:
            pygame.draw.rect(display, rect[0], rect[1])

        pygame.display.update()
        clock.tick(CLOCK)

if __name__ == "__main__":
    main()