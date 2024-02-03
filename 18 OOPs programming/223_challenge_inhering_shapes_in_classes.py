import math
class Polygon:
        def __init__(self,ns,*sides):
            self.num_of_sides=ns
            self.sides=sides[:ns] #if you give more positioNAL argument then unpacking error will arise. so llimit it to ns


class Traingle(Polygon):
        def __init__(self, tri_ns,*tri_sides):
            Polygon.__init__(self,tri_ns,*tri_sides) 
            #super().__init__(ns, *sides) 
        
        def area(self):
            print(self.sides)
            a,b,c=self.sides #unpacking

            s=(a+b+c)/2
            area=math.sqrt(s * (s-a) * (s-b) * (s-c))
            return area
        
class Rectangle(Polygon):
        def __init__(self, rec_ns,*rec_sides):
            super().__init__(rec_ns,*rec_sides)

        def area(self):
            print(self.sides)
            a,b,c,d=self.sides #unpacking

            s=(a+b+c+d)/2
            area=math.sqrt(s * (s-a) * (s-b) * (s-c) * (s-d))
            return area
        
t1=Traingle(3,10,15,9) #writting to many args wont cause error
print(t1.area())

r1=Rectangle(4,10,20,10,20) #may be error in logic but method is write
print(r1.area())