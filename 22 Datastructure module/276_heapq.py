'''
It will work as a priority queue . It will gives you the highest priority element 
Smaller the number will be the highest priority so 10 has the highest priority and 70 will be the least priority

the heapq module in Python is designed to maintain
the smallest element at the front of the heap 
(usually the root of the heap tree). 
It efficiently allows you to push elements onto the heap and pop the smallest element. 
However, it does not guarantee any specific order for the remaining elements in the heap, 
especially for elements with equal priority. 
->heapq
->heappush
->heappop
->heapreplace
->heap
->nlargest
->nsmallest
'''
import heapq
l1=[30,20,10,50,40,70,60]
heapq.heapify(l1)
print(1,l1) #rearrange from smallest to largest

l2=list()

heapq.heappush(l2,40)
print(2,l2)
heapq.heappush(l2,30)
print(3,l2)
heapq.heappush(l2,10)
heapq.heappush(l2,60)
heapq.heappush(l2,50)
heapq.heappush(l2,20)
print(4,l2)

print(5,l2)
heapq.heappop(l2)
print(6,l2) #highest priority element will be removed
heapq.heappop(l2)
print(7,l2)

print(8,heapq.nlargest(2,l2))
print(9,heapq.nsmallest(3,l2))

print(10,heapq.heapreplace(l1,11))
'''
The heapreplace function in the heapq module is used
to replace the smallest element in a heap with a new value.
It is similar to a combination of heappop followed by heappush. 
The advantage of using heapreplace over these two operations is
that it can be more efficient 
since it only performs the necessary reorganization of the heap once.'''
print(l1)