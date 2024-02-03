class customer:
    def __init__(self,id,name,billing_no,billing_addr,billing_pin,shipping_no,shipping_addr,shipping_pin):
        self.cust_id=id
        self.cust_name=name
        self.b_addr=self.Address(billing_no,billing_addr,billing_pin) #address is member of class
        self.s_addr=self.Address(shipping_no,shipping_addr,shipping_pin)

    class Address:
        def __init__(self,no,addr,pin):
            self.number=no
            self.address=addr
            self.pin=pin

        def display(self):
            print(self.pin,self.address,self.number)

c1=customer(150760109064,'abhu',12,'kamrej',101,21,'adajan',201)
c1.s_addr.display() 
print(c1.cust_id)
print(c1.cust_name)
    
