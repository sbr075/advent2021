"""
Written fast just to see how the puzzle looks like visually
"""

import pygame
import numpy as np
from puzzle2 import read_input
import time

MAIN_TEXT = (32, 120, 24)
FLASHES = (163, 31, 219)
DORMENT = (42, 9, 56)
BACKGROUND = (12, 29, 56)

SCREEN_X = 800
SCREEN_Y = 800
RESOLUTION = (SCREEN_X, SCREEN_Y)

pygame.init()
pygame.display.set_caption("Flashing octopuses")
display = pygame.display.set_mode(RESOLUTION)

MAIN_FONT = pygame.font.SysFont("consolas", 20, bold=True)

clock = pygame.time.Clock()
def main():
    data = np.array(read_input())

    display.fill(BACKGROUND)
    step = 0
    tot_flashes = 0

    # checkpoints
    flashes_100s = 0
    steps_100f = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        flashes = 0
        data=np.add(data, 1)
        while (data > 9).sum() > 0:
            for y in range(len(data)):
                for x in range(len(data[y])):
                    r = pygame.Rect(40+((SCREEN_Y - 20) / 10)*y, 80+((SCREEN_X - 60) / 10)*x, 20, 20)
                    if data[y,x] < 10:
                        pygame.draw.rect(display, DORMENT, r)
                    else:
                        data[max(0,y-1):y+2, max(0,x-1):x+2] += 1
                        data[y,x] = -10
                        pygame.draw.rect(display, FLASHES, r)

        flashes = (data < 0).sum()
        tot_flashes += flashes
        step+=1

        display.fill(BACKGROUND, rect=(0,0, SCREEN_X, 70))

        step_txt = MAIN_FONT.render(f"Step(s): {step}", True, MAIN_TEXT)
        flashes_txt = MAIN_FONT.render(f"Total flashes: {tot_flashes}", True, MAIN_TEXT)
        if step == 100:
            flashes_100s = tot_flashes
            flashes_100s_txt = MAIN_FONT.render(f"Flashes at step 100: {flashes_100s}", True, MAIN_TEXT)
        
        if flashes_100s != 0:
            display.blit(flashes_100s_txt, (300, 10))
        
        if flashes == 100:
            steps_100f = step
            steps_100f_txt = MAIN_FONT.render(f"First time all octopuses flashed: {steps_100f}", True, MAIN_TEXT)
        
        if steps_100f != 0:
            display.blit(steps_100f_txt, (300, 30))

        display.blit(step_txt, (30, 10))
        display.blit(flashes_txt, (30, 30))
        
        data[data < 0] = 0

        pygame.display.update()
        clock.tick(20)

        if flashes == 100:
            time.sleep(5)
            break


if __name__ == "__main__":
    main()