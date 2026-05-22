class Warrior:

    def __init__(self, stren, h):
        self.__strenght = stren
        self.__hp = h

    @property
    def get_strenght(self):
        return self.__strenght


    @get_strenght.setter
    def get_set_strength(self, stren):
        if stren == "":
            raise ValueError("xxxxxxxx")
        self.__strenght = stren

W = Warrior(10, 8)
print(W.get_strenght)
W.get_set_strength = 20
#(W.get_set_strength)
print(W._Warrior__strenght)







import math

class Circle:
    def __init__(self, ra):
        self.radius = ra

    @property
    def ci(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.ci)
print(c.area)

