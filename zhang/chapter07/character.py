class Warrior:
    def __init__(self, name, strenght, hp):
        self.name = name
        self.strenght = strenght
        self.hp = hp


    def info(self):
        print(f"name:", self.name)
        print(f"strenght:", self.strenght)
        print(f"hp:", self.hp)

WA = Warrior("A", 10, 10)
WA.info()


