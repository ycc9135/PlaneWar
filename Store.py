import random as r


class Store:
    def __init__(self, maxNum):
        # 一条记忆：环境，动作，奖励，下一个环境
        self.stores = []
        self.maxNum = maxNum
        self.curIndex = 0

    def add(self, s, a, r, s_):
        if len(self.stores) == self.maxNum:
            self.stores[self.curIndex] = [s, a, r, s_]
            self.curIndex += 1
            if self.curIndex == self.maxNum:
                self.curIndex = 0
        else:
            self.stores.append([s, a, r, s_])

    def sample(self, batch):
        res = r.sample(self.stores, batch)
        return res
