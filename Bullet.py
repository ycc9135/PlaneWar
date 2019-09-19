from PlaneWar.Shape import *


class Bullet(Shape):
    def __init__(self):
        super(Bullet, self).__init__(0, 0, [
            (0, 0)
        ])

    def move(self, map):
        if self.checkOutOfMap(self.x, self.y - 1, map) == 2:
            return False
        else:
            self.setxy(self.x, self.y - 1)
            return True
