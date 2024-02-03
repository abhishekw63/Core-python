'''
->There is a module available in python that is used for storing and retrieving objects of a class
->The process of storing multiple objects of a class in a single file is called Pickle
->To read the entire object of a class at once is called Unpickle.
->Therefore, storing an object in a file is Pickle , Retrieving an object from a file is called Unpickle
->The pickle module provides a function called  Dump  , which will store the contents in a file 
->Pickling is always done in Binary Mode
->The function called Load is used to read the file as well
'''

#creating a instance of class:part 1
#   ->196_pickle_unpickle
class Students:
    def __init__(self,roll_no,name,dept): #instance variable
        self.roll_no=roll_no
        self.name=name
        self.dept=dept
    def display(self):
        print(f'Roll no:{self.roll_no} Name:{self.name} Department:{self.dept}')
#https://chat.openai.com/c/93b5656a-c42d-42d2-b0a0-eff373ad2a8b

