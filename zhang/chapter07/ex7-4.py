import random

class Warrior:
    count = 0

    def __init__(self, strenght, luc, level):
        self.__strenght = strenght
        self.__luc = luc
        self.level = level
        # self.__class__.count += 1

    # @classmethod
    # def xxx(cls):
    #     return cls.count

    @property
    def luc_get(self):
        return self.__luc

    @property
    def strenght_get(self):
        return self.__strenght

    @luc_get.setter
    def luc_get_set(self, setluc_v):
        self.__luc = setluc_v
        return self.__luc

    @strenght_get.setter
    def strenght_get_set(self, setstrenght_v):
        self.__strenght = setstrenght_v
        return self.__strenght


    def attack(self):
        if self.luc_get >= random.random():
            print("True")
        else:
            print("False")




class Thief(Warrior):
    def steal(self):
        self.luc_get_set += 0.1


class Knight(Warrior):
    def charge(self):
        self.strenght_get_set += 2

    def attack(self):
        super().attack()
        self.strenght_get_set *= 2
        self.level += 1
        print(self.strenght_get_set)
        print(self.level)

K = Knight(10, 10, 1)
K.attack()
K.attack()
K.attack()

