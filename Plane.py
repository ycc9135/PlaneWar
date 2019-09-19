from PlaneWar.Shape import *
from PlaneWar.Bullet import *


class Plane(Shape):
    def __init__(self, cd):
        super(Plane, self).__init__(2, 0, 0, [
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
            (-2, -3),
            (2, -3)
        ])
        self.bullets = []
        self.alive = True
        self.cd = cd
        self.fireN = cd
        self.speed = 1

    def goleft(self, map):
        if self.checkOutOfMap(self.x - self.speed, self.y, map) == 0:
            self.setxy(self.x - self.speed, self.y)

    def goright(self, map):
        if self.checkOutOfMap(self.x + self.speed, self.y, map) == 0:
            self.setxy(self.x + self.speed, self.y)

    def goup(self, map):
        if self.checkOutOfMap(self.x, self.y - self.speed, map) == 0:
            self.setxy(self.x, self.y - self.speed)

    def godown(self, map):
        if self.checkOutOfMap(self.x, self.y + self.speed, map) == 0:
            self.setxy(self.x, self.y + self.speed)

    def fire(self):
        if self.fireN >= self.cd:
            bullet = Bullet()
            bullet.setxy(self.x, self.y + self.dtop - 1)
            self.bullets.append(bullet)
            self.fireN = 0
