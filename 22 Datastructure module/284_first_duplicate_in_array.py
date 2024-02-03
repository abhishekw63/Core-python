import array


def find_duplicate(arr):
    new_set=set()
    
    for item in arr:
        if item not in new_set:
            new_set.add(item)
        else:
            return item
    else:
        return -1 #if no duplicate found return -1
ar1=array.array('i',[2,4,6,7,8,10,4,12,10,20]) #try 4 changing to 40
print(find_duplicate(ar1))