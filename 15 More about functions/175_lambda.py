'''
->Anonymous function.
->Single line expression.
->Any number of argument.
'''

k=lambda miles:1.6 * miles
print('miles to km',k(1))

p=lambda a,b:a if a>b else b
print('max from 2:',p(100,20))



# # Get the list of all keywords
# all_keywords = keyword.kwlist

# # Print the list of keywords
# print("List of Python Keywords:")
# print(len(all_keywords))

# # Print the total number of keywords
# print("\nTotal number of keywords:", len(all_keywords))


# from datetime import datetime

# current_date = datetime.now().date()
# print("Current date:", current_date)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)

# Convert the iterator to a list to see the result
result_list = list(zipped)
print(result_list)
