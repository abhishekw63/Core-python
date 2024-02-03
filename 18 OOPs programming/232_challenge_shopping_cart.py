'''
->overriding
'''

class Shopping:
    def __init__(self):
        self.cart=list()

    def add_to_cart(self,item):
        self.cart.append(item)

    def remove_from_cart(self,item):
        self.cart.remove(item)
    def __len__(self):
        return len(self.cart)
    def __str__(self):
        items=''
        print('items are:',end='')
        for i in self.cart:
            items+=i+','
        return items
    
c1=Shopping()
c1.add_to_cart('soap')
c1.add_to_cart('l3mon')
c1.add_to_cart('bottle')
c1.add_to_cart('paste')
print(c1)

c1.remove_from_cart('soap')
print(c1)

print(len(c1))