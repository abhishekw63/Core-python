import collections

price={'toothpaste':15,'soap':5.5,'shampoo':32.9,'brush':10.2}

cart=collections.Counter(toothpaste=1,soap=5,shampoo=8,brush=10)

print(f'{"product":<25}{"price":^10}{"subtotal":>15}')

def generate_bill(cart):
    total=0 
    for item,qty in cart.items():
        print(f'{item:<20}{"X":<5}{price[item]:^10}{"=":^5}{qty*price[item]:^10}')
        total+=qty*price[item] 
    print('-'*50)       
    print(f'{"total is:":<42}{total}')
        

generate_bill(cart)
        