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
                if self.data[i][j][0] == 1:
                    pg.draw.rect(self.screen, WHITE, (
                        j * self.cellSize,
                        i * self.cellSize,
                        self.cellSize,
                        self.cellSize
                    ), 0)
