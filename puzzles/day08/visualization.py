"""
This is not a true visualization because all computation is done before
the visualization even begins. The program just loops through lines and updates
the numbers one by one creating a fun effect to watch

Oh, and, it was written at 2am because I got the idea then so do not judge
me by the code :)
"""

import pygame
from puzzle2 import read_input, get_ttbl
import random

MAIN_TEXT = (32, 120, 24)
MAIN_TEXT_DONE = (56, 201, 42)

DECRYPTED = (56, 230, 42)
ENCRYPTED = (120, 34, 14)
SCANNING  = (191, 53, 21)
BACKGROUND = (10, 10, 10)

SCREEN_X = 800
SCREEN_Y = 800
RESOLUTION = (SCREEN_X, SCREEN_Y)

pygame.init()
pygame.display.set_caption("Decoder")
display = pygame.display.set_mode(RESOLUTION)

MAIN_FONT = pygame.font.SysFont("consolas", 18, bold=True)
BASE_FONT = pygame.font.SysFont("consolas", 15)

MAX_LINES = 20

# If set to false it will only "solve" the first MAX_LINES of the data
SCROLL = False

clock = pygame.time.Clock()
def main():
    data = read_input()
    tmp = read_input()
    if not SCROLL:
        data = data[:MAX_LINES]
        tmp = tmp[:MAX_LINES]

    main_done = []
    unsolved = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(len(data))]

    ttbls = []
    for d in tmp:
        ttbls.append(get_ttbl(d[0]))

    line = 0
    solved_before_scroll = int(MAX_LINES/2)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        """
        Logic
        1. Select random number to "solve"
        2. Find what word number corresponds to in the solved version
        3. Find index of word in indata
        4. Switch places
        """

        # Select a random number to "solve" from current line
        if any(unsolved):
            # Fills the screen
            display.fill(BACKGROUND)

            ttbl = ttbls[line]
            switch1 = random.choice(unsolved[line])
            for k, v in ttbl.items():
                if v == switch1:
                    s = k

            for i in range(MAX_LINES):
                if SCROLL:
                    idx = (i+line-int(MAX_LINES/2)+solved_before_scroll)%len(data)
                else:
                    idx = i
                indata = data[idx][0]

                # For each "word" in indata
                for j in range(len(indata)):
                    if j in unsolved[idx]:
                        if idx == line:
                            if j == switch1:
                                # Fetch index of where the real answer is in current list
                                unsolved[idx].remove(switch1)
                                done = True
                                for u in unsolved:
                                    if switch1 in u:
                                        done = False
                                        break
                                
                                if done: main_done.append(switch1)

                                switch2 = indata.index(s)
                                
                                indata[switch2] = indata[switch1]
                                indata[switch1] = s

                                color = DECRYPTED
                            else:
                                color = SCANNING
                        else:
                            color = ENCRYPTED
                    else:
                        color = DECRYPTED

                    text = BASE_FONT.render(indata[j], True, color)
                    display.blit(text, (10+((SCREEN_X - 20) / 10)*j, 40+((SCREEN_Y - 50) / MAX_LINES)*i))

            for i in range(10):
                color = MAIN_TEXT if i not in main_done else MAIN_TEXT_DONE
                text = MAIN_FONT.render(str(i), True, color)
                display.blit(text, (10+((SCREEN_X - 10) / 10)*i, 10))

            line += 1
            line %= len(data)

            if solved_before_scroll > 0:
                solved_before_scroll -= 1

        pygame.display.update()
        clock.tick(15)


if __name__ == "__main__":
    main()