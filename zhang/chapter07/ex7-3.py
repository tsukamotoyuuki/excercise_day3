import random

class Warrior:
    count = 0

    def __init__(self, luc):
        self.__luc = luc
        self.__class__.count

    @classmethod
    def xxx(cls):
        return cls.count

    @property
    def luc_get(self):
        return self.__luc

    @luc_get.setter
    def luc_get_set(self, setluc_v):
        self.__luc = setluc_v
        return self.__luc

W = Warrior(random.random())
print(W.luc_get)
W.luc_get_set = 2000
print(W.luc_get_set)



