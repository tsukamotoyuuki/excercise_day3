class Book:
    def __init__(self,title="",author=""):
        self.title = title
        self.author = author

    def info(self):
        print(f'タイトル:{self.title},著者：{self.author}')


book = Book('A Greet Book','tanaka')
book.info()