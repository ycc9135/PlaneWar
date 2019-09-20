import pygame as pg
from PlaneWar.Colors import *


class Map:
    def __init__(self, screen, width, height, cellSize):
        self.data = []
        self.screen = screen
        self.cellSize = cellSize
        self.w = int(width / cellSize)
        self.h = int(height / cellSize)

        for i in range(self.h):
            lineData = [[0] for _ in range(self.w)]
            self.data.append(lineData)

    def draw(self):
        for i in range(self.h):
            for j in range(self.w):
                d = self.data[i][j][0]
                if d != 0:
                    c = BLACK
                    # c = 1
                    if d == 1:
                        c = WHITE
                    elif d == 2:
                        c = BLUE
                    elif d == 3:
                        c = RED

                    elif d == 4:
                        c = DeepPink
                    elif d == 5:
                        c = DarkMagenta
                    elif d == 6:
                        c = DoderBlue
                    elif d == 7:
                        c = DarkRed
                    pg.draw.rect(self.screen, c, (
                        j * self.cellSize,
                        i * self.cellSize,
                        self.cellSize,
                        self.cellSize
                    ), 0)
