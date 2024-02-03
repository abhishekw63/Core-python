from collections import deque

customers=deque()

def walk_in(customer):
    customers.append(customer)

def serviced():
    cust=customers.popleft() #FIFO fashion
    print(cust,' is leaving.')
    
walk_in('raj')
walk_in('abhishek')
serviced()
walk_in('shivam')
walk_in('nilesh')
serviced()
serviced()
walk_in('ashish')
walk_in('mitesh')
serviced()
print(customers) #these are remains