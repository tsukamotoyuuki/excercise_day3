class Book:
    def __init__(self, title="", author=""):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author

    def info(self):
        print(f"タイトル: {self.__title}, 著者: {self.__author}")
        return 0


b1 = Book("Princess_Kaguya", "???")
b1.info()
