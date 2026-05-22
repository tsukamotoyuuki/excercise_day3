# # 1-1
# class Book:
#     def __init__(self, title, author):
#         self.title = str(title)
#         self.author = str(author)
#
# B = Book("python", "AAA")


# 1-2
class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

    def info(self):
        print("タイトル: " + self.title)
        print("著者: " + self.author)

# 1-3
B = Book("python", "AAA")
B.info()


