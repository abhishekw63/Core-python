'''
Double ended queue:
Queue FIFO
Stack:LIFO
->append
->appendleft
->count
->extendleft
->index
->insert
->pop
->popleft
->remove
->reverse
->rotate
'''
'''import collections
import pprint
pprint.pprint(dir(collections))'''

from collections import deque

l1=[5,6,7,8,9,10]

dq=deque(l1)
print(1,dq)

dq.append(11) #appending at rhs
print(2,dq)

dq.appendleft(12)# appending at lhs
print(3,dq)

dq.pop()# deleted from rhs
print(4,dq)

dq.popleft()#deleted from lhs
print(5,dq)

dq.extend([13,14,15,16])#13->14->15->16(last one)
print(6,dq)

dq.extendleft([17,18,19,20]) #20->19->18->17 (first one)
print(7,dq)

dq.rotate(3) #if rotate(1): l1=[1,2,4,5] -> l1=[5,1,2,4]
print(8,dq) #if rotate(2): l1=[1,2,3,4,5] -> l1=[5,4,1,2,3]

dq1=dq.count(14) # count the number of occurrences of a specific element in the deque. 
print(9,dq1)

print(10,dq.index(15)) #returns an index

dq.insert(0,100)
print(11,dq)

dq.reverse()
print(12,dq)