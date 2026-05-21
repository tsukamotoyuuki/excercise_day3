class Book:
    def __init__(self, title="", author=""):
        self.__title = title
        self.__author = author

    def info(self):
        print("タイトル:" + self.__title)
        print("著者:" + self.__author)


if __name__ == "__main__":
    b1 = Book("abcde", )
    b1.info()


