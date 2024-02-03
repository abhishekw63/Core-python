#part 3:retrieving objects

import pickle
import Student_class as s_class

with open('students.data','rb') as f:
    for _ in range(0,3): #if dont know object number then execute using exception EOFError with while loop
        student=pickle.load(f)
        #print(student) #returns a three separate object
        student.display()