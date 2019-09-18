from PlaneWar.Shape import *


class Stone(Shape):
    def __init__(self):
        super(Stone, self).__init__(0, 0, [
            (0, 0),
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ])
