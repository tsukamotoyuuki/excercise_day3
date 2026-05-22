class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age  = age

    def greet(self):
        print("Hello,my name is " + self.__name)


alice = Person("Alice", 23)
bob   = Person("Bob", 30)

alice.__name = "Alice2"
alice.greet()
bob.greet()


# class people:
#     name = "aaaaaaaa"
#     age = 0
#
#     def __init__(self, n, a):
#         self.name = n
#         self.age  = a
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#
#
# p = people('runoob', 10)
# p.speak()
# print(p.name)
# print(p.age)
