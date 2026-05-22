import random

class Warrior:
    count = 0
    percent = 0
    def __init__(self,name,strength,hp):
        self.__strength = strength
        self.__hp = hp
        self.__name = name
        self.__luc = random.random()
        Warrior.count += 1

    def attack(self):
        self.__class__.percent = random.random()
        if self.__class__.percent < self.luc:
            success = True
        else:
            success = False
        return {"at": self.strength, "suc": success}
    def info(self):
        print('name:'+self.__name)
        print(f'strength:{self.__strength}')
        print(f'hp:{self.__hp}')
        print(f'luc:{self.__luc}')


    @property
    def luc(self):
        return self.__luc

    @luc.setter
    def luc(self, value):
        if value == '':
            raise ValueError("luc 不能为空")
        self.__luc = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value == '':
            raise ValueError("strength 不能为空")
        self.__strength = value

    @classmethod
    def print_count(cls):
        return cls.count





class Thief(Warrior):
    def steal(self,luc):
        self.luc += 0.1

class Knight(Warrior):
    def charge(self):
        self.strength += 2
    def attack(self):
        result = super().attack()
        result["at"] *= 2
        return result


if __name__ == "__main__":
    wA = Warrior("A", 10, 10)
    wA.info()
    print(wA.attack())
    wB = Knight("B", 11, 11)
    wB.info()
    print(wB.attack())

