class Shape:
    def __init__(self,color):
        self.color = color

    def desc(self):
        return f'この図形の色は{self.color}です。'

class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height

    def desc(self):
        return f"この図形の色は{self.color}で幅は{self.width}、高さは{self.height}です。"

    def arrea(self):
        return self.width * self.height

a = Rectangle('Blue',30,40)
print(a.desc())
print("面積は",a.arrea(),"です。")
