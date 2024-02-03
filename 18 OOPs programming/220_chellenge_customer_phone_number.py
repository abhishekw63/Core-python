class Customer:
    def __init__(self,c_name,c_phn_num):
        self.name=c_name
        self.phn_num=int(c_phn_num)
    def get_name(self): #accessors
        return self.name
    def get_phn_num(self):#accessors
        return self.phn_num
    def set_phn_num(self,new_phn_num):
        self.phn_num=int(new_phn_num)

c1=Customer('abhi','1234')
print(c1.get_name())
print(c1.get_phn_num())
c1.set_phn_num('98762')
print(c1.get_phn_num())