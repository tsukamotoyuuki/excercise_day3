class Person:

    def __init__(self, name, age):
        self.name = name  # ✅ 会调用 setter
        self.age = age

    @property
    def name(self):
        print("name  getter")
        return self.__name

    @aaa.setter
    def name(self,name):
        print("name setter")
        if name == "":
            raise ValueError("name is empty")
        self.__name = name



alice = Person("Alice",23)
print(alice.name)
alice.name = "dddddd"

