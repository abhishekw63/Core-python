'''
->built in list in python is heterogenous i.e. allowed different datatypes
->but array module is homogenous
->when you want to make sure that element is homogenous then go for array
code        type        minimum size(bytes)
b           int             1
B           unsigned int    1
i           s int           2
I           us int          2
l           s long          4
L           us long         4   
q           s long long     8
Q           u long long     8
f           float           4              
D           double float    8
->arrayName=array.array(type,[aray_items])
#we can perform on operations on array items as done in list tup dict
'''
import array
ar1=array.array('i',[10,20,30,40])
print(1,ar1)

s1=b'abcdef'
print(2,array.array('b',s1))

uint=array.array('I',[10,20,30,40,50])
print(3,uint)

long_array = array.array('l', [100, 200, 300, 400, 500])
print(f"Signed Long Array: {long_array}")

# Unsigned long
ulong_array = array.array('L', [1000, 2000, 3000, 4000, 5000])
print(f"Unsigned Long Array: {ulong_array}")

# Signed long long
long_long_array = array.array('q', [10000, 20000, 30000, 40000, 50000])
print(f"Signed Long Long Array: {long_long_array}")

# Unsigned long long
ulong_long_array = array.array('Q', [100000, 200000, 300000, 400000, 500000])
print(f"Unsigned Long Long Array: {ulong_long_array}")

# Float
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print(f"Float Array: {float_array}")

# Double
double_array = array.array('d', [1.111, 2.222, 3.333, 4.444, 5.555])
print(f"Double Array: {double_array}")

# Character
char_array = array.array('b', b'hello')
print(f"Character Array: {char_array}")


print('sum:',sum(ar1))
print('slice',ar1[1:3])
'''

In Python, both arrays and lists are used to store collections of elements. However, there are key differences:

Homogeneity: Arrays are homogeneous, meaning they can only store elements of the same data type, while lists can contain elements of different types.

Memory Efficiency: Arrays are more memory-efficient than lists when dealing with large datasets of numeric values because they use a fixed, compact memory allocation for a specific data type.

Operations: Lists offer more built-in methods and functionalities compared to arrays. Lists are more versatile and provide a wide range of operations, making them easier to work with for general-purpose tasks.

Flexibility: Lists are more flexible due to their ability to store mixed data types and dynamic resizing. Arrays, on the other hand, have a fixed size and type.

In summary, arrays are advantageous when dealing with numerical data and memory efficiency is crucial, while lists are more versatile and convenient for general-purpose programming tasks.
'''

'''
import array

# List of integers
my_list = [1, 2, 3, 4, 5]

# Array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

print(my_list.__sizeof__())  # Size of list in bytes
print(my_array.__sizeof__())  # Size of array in bytes

'''