from PlaneWar.Shape import *


class Plane(Shape):
    def __init__(self):
        super(Plane, self).__init__(0, 0, [
            (0, 0),
            (0, -1),
            (0, -2),
            (0, -3),
            (-1, 0),
            (1, 0),
            (-1, -2),
            (-2, -2),
            (1, -2),
            (2, -2),
        ])

    def goleft(self, map):
        if self.checkOutOfMap(self.x - 1, self.y, map) == 0:
            self.setxy(map, self.x - 1, self.y)

    def goright(self, map):
        if self.checkOutOfMap(self.x + 1, self.y, map) == 0:
            self.setxy(map, self.x + 1, self.y)

    def goup(self, map):
        if self.checkOutOfMap(self.x, self.y - 1, map) == 0:
            self.setxy(map, self.x, self.y - 1)

    def godown(self, map):
        if self.checkOutOfMap(self.x, self.y + 1, map) == 0:
            self.setxy(map, self.x, self.y + 1)
