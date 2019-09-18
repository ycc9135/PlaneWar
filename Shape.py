class Shape:
    def __init__(self, x, y, dertCellList):  # [(0,-1),(1,0)]
        self.x = x
        self.y = y
        self.dertCellList = dertCellList

        self.dtop = 9999
        self.dbottom = -9999
        self.dleft = 9999
        self.dright = -9999
        for a, b in dertCellList:
            if a > self.dright:
                self.dright = a
            if a < self.dleft:
                self.dleft = a
            if b > self.dbottom:
                self.dbottom = b
            if b < self.dtop:
                self.dtop = b

    def getCellList(self):
        return [(x[0] + self.x, x[1] + self.y) for x in self.dertCellList]

    def putInMap(self, map):
        cellList = self.getCellList()
        for x, y in cellList:
            map.data[y][x][0] = 1

    def removeFromMap(self, map):
        cellList = self.getCellList()
        for x, y in cellList:
            map.data[y][x][0] = 0

    def setxy(self, map, x, y):
        self.removeFromMap(map)
        self.x = x
        self.y = y
        self.putInMap(map)

    def checkOutOfMap(self, x, y, map):
        if x + self.dleft < 0:
            return 1
        elif x + self.dright >= map.w:
            return 3
        elif y + self.dtop < 0:
            return 2
        elif y + self.dbottom >= map.h:
            return 4
        else:
            return 0

    def checkAABB(self, other):
        scl = self.getCellList()
        ocl = other.getCellList()
        for xy in scl:
            if xy in ocl:
                return True
        return False

