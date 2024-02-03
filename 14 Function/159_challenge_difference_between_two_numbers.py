def diff(x,y):
    if abs(x-y)<=5:
        return True
    else:
        return False

print(diff(15,25)) # result would be -5 if you dont write abs. 
