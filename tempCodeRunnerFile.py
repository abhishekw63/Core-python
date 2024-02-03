#factorial recursion

def recuraion(n):
    if n==0:
        return 1
    else:
        return n * recuraion(n-1)
    
print(recuraion(10))