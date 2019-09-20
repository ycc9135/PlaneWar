from PlaneWar.Shape import *
import random as r
import random


class Stone(Shape):
    def __init__(self):
        super(Stone, self).__init__(random.randint(3,7), 0, 0, [
            (0, 0),
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ])
        self.dir = r.randint(1, 3)

    def move(self, map):
        if self.dir == 1:
            omp = self.checkOutOfMap(self.x - 1, self.y + 1, map)
            if omp == 1:
                self.dir = 3
            elif omp == 4:
                return False
            else:
                self.setxy(self.x - 1, self.y + 1)
        elif self.dir == 2:
            omp = self.checkOutOfMap(self.x, self.y + 1, map)
            if omp == 4:
                return False
            else:
                self.setxy(self.x, self.y + 1)
        elif self.dir == 3:
            omp = self.checkOutOfMap(self.x + 1, self.y + 1, map)
            if omp == 3:
                self.dir = 1
            elif omp == 4:
                return False
            else:
                self.setxy(self.x + 1, self.y + 1)
        return True
