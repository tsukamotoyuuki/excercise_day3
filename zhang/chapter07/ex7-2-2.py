# 2-1
class Shape:
    def __init__(self, color):
        self.color = str(color)

    def desc(self):
        print("この図形の色は " + self.color + " です。")

S = Shape("red")
S.desc()


# 2-2 と　2-3
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def desc(self):
        print("この図形の色は " + self.color + " で幅は " + str(self.width) + " 、高さは " + str(self.height) + " です。")


arrea = Rectangle("green", 12, 6)
arrea.desc()

