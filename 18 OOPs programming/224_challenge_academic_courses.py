class Course:
    def __init__(self,name,duration,*book):
        self.c_name=name
        self.c_duration=duration
        self.c_books=[self.Book(b) for b in book] #LIST OF instances of book

    def show(self):
        print(f'Name:{self.c_name} Duration:{self.c_duration} ')
        #print(f'Books:{[str(b) for b in self.c_books]}')
        for b in self.c_books:
            print(b)
    
    class Book:
        def __init__(self,title):
            self.title=title

        def __str__(self):
            return self.title

c1=Course('Backend','6 Month','c','c++','sql','python','django')
c1.show()