#students queue is based on roll number
#rotate queue in every meal

from collections import deque

l1=deque([2,4,5,6,7,9,10,34,65,89,100])

print('Students queue is:',l1)
def serve_food():
    l1.rotate(-1) #giving 1 will rotate it from right to left, can give 2 3 or 4 step
    print(l1)

print('Queue for lunch:',serve_food())
print('Queue for dinner:',serve_food())
print('Queue for breakfast:',serve_food())