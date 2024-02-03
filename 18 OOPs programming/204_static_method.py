class cuboid:
    def __init__(self,l=1,b=1,h=1): 
        self.length=l 
        self.breadth=b
        self.height=h

    def volume(self): 
        return self.length*self.breadth*self.height
    def total_area(self):
        return 2*(self.length*self.breadth + self.breadth*self.height + self.height*self.length)    
    def lidarea(self):
        return self.length*self.breadth
    
    @staticmethod
    def iscuboid(len,bre,hei): #it is not accessing any instance varibale or the class variable->static methods
        return len==bre==hei
    
c1=cuboid(10,20,30)
print(c1.iscuboid(1,1,1)) #return true.static method is accessed through object varible
print(cuboid.iscuboid(1,1,3))#also called with class name.it is preferable because those methods are just present inside the class