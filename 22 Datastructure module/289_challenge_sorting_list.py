import bisect

def sorting_list(elements):
    sorted_list=[]
    
    for item in elements:
        bisect.insort(sorted_list,item)
        #print('\u2605',sorted_list)
        
    return sorted_list
elements=[7,8,9,4,5,6,3,2,1]
print('Sorting via elements',sorting_list(elements))