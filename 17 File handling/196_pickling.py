#part 2: storing an objects

import Student_class as s_class
import pickle

obj_list=[s_class.Students(101,'abhishek','Ele'),s_class.Students(102,'raj','Mech'),s_class.Students(103,'rohan','computer')]

with open('students.data','wb') as f:
    for item in obj_list:
        pickle.dump(item,f)



# A byte stream is a sequence of bytes. 
# In Python, when you open a file in binary mode ('rb' for reading or 'wb' for writing), the data read from or written to the file is treated as a byte stream. 
# This means that data is represented as a sequence of bytes, which can be manipulated or processed by the program.
# In the context of pickling, the serialized object is converted into a byte stream before being written to a file, and this byte stream is then reconstructed back into the original object during unpickling.

# import pickle

# # Example dictionary to pickle
# data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# # Pickling: Serialize the data and save it to a file
# with open('data.pkl', 'wb') as f:
#     pickle.dump(data, f)

# # Unpickling: Deserialize the data from the file
# with open('data.pkl', 'rb') as f:
#     loaded_data = pickle.load(f)

# print(loaded_data)
