import heapq

def sorting_through_heap(elements):
    heapq.heapify(elements)
    sorted_list=[]
    '''for item in elements: removing an item and appendingis leading to issue
        sorted_list.append(heapq.heappop(elements))'''
    while elements:
        sorted_list.append(heapq.heappop(elements))
    return sorted_list

elements=[3,6,2,1,8,-5,-3,45,-2]
print('sorting through heap:',sorting_through_heap(elements))