class Shape:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def desc(self):
        return f"この図形の色は {self.__color} です。"


class Rectangle(Shape):
    def __init__(self, color, width: int, height: int):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def desc(self):
        return f"この図形の色は {self.color} で幅は {self.__width}、 高さは {self.__height} です。"

    def area(self):
        return self.__height * self.__width


r = Rectangle("red", 10, 10)
print(r.desc())
print(r.area())
