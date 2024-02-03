class CC:
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
    def get_c_name(self):
        return self.name
    def get_c_rate(self):
        return self.rate
    def set_c_name(self,new_name):
        self.name=new_name
    def set_c_rate(self,new_rate):
        self.rate=new_rate

    def conversion(self,amount):
        return f'{self.name} to IND conversion is:{self.rate*amount}'

c1=CC('US',100)
print(c1.get_c_name())
print(c1.conversion(50))

c1.set_c_name('PKR')
c1.set_c_rate(0.5)
print(c1.conversion(100))
