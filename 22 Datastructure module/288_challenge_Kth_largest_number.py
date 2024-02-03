import heapq

def kth_largest(elements,k):
    sorted_list=[]
    for item in elements:
        heapq.heappush(sorted_list,-item)
    
    for item in range(k-1): #if you want 3rd largest one then first two need to be removed then automatically 0th element will be result
        heapq.heappop(sorted_list)
        
    return -heapq.heappop(sorted_list)
        
elements=[4,6,3,64,23,56,2,54,66,22,27]
print('kth largest element is',kth_largest(elements,4))