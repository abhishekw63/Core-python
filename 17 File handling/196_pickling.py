#part 2: storing an objects

import Student_class as s_class
import pickle

obj_list=[s_class.Students(101,'abhishek','Ele'),s_class.Students(102,'raj','Mech'),s_class.Students(103,'rohan','computer')]

with open('students.data','wb') as f:
    for item in obj_list:
        pickle.dump(item,f)

