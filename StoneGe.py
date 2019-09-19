from PlaneWar.Stone import *
import random as r


class StoneGe:
    def __init__(self, map, totalNum, frameNum):
        self.totalNum = totalNum
        self.stones = []
        self.frameNum = frameNum
        self.n = 0
        self.map = map

    def run(self):
        self.n += 1
        if self.n >= self.frameNum and len(self.stones) < self.totalNum:
            stone = Stone()

            x, y = r.randint(-stone.dleft, self.map.w - 1 - stone.dright), -stone.dtop
            stone.setxy(x, y)
            self.stones.append(stone)
            self.n = 0
