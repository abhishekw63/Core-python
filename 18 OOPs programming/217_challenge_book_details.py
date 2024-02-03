class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def show(self):
        print(f'Title:{self.title}\nAuthor:{self.author}\nPrice:{self.price}')

b1=Book('Python','Abhishek',100)
b1.show()
