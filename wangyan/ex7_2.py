class Warrior:
    def __init__(self,name,strength,hp):
        self.__strength = strength
        self.__hp = hp
        self.__name = name
    def info(self):
        print('name:'+self.__name)
        print(f'strength:{self.__strength}')
        print(f'hp:{self.__hp}')

    @property
    def name(self):
        return self.__name

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value == '':
            raise ValueError("strength 不能为空")
        self.__strength = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value <= 0:
            raise ValueError("hp 必须 > 0")
        self.__hp = value


if __name__ == "__main__":
    alice = Warrior('A',10,10)
    alice.info()