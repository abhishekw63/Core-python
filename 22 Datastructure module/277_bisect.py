'''
->This will maintain the list in stored order.
It can have duplicate numbers.
If you want to perform intersection operations ,
but it will ensures that the list is a sorted order .

->
'''
import bisect
l1=[10,20,30,40,50,60,70,80] #preserved it state

bisect.insort(l1,35) 
print(1,l1)

bisect.insort(l1,65,lo=5,hi=len(l1)) #lo and hi are index
print(2,l1)

bisect.insort_left(l1,20) #add 20 at index 1
print(3,l1)
#likwise insort_right


print(4,bisect.bisect(l1,1)) #where will 70 be added? at 0 index
print(5,bisect.bisect_right(l1,80)) #what will be index number if added right side 

bisect.insort_left(l1,80) 
print(6,id(l1[10]),7,id(l1[11])) #both object referring to same integer
