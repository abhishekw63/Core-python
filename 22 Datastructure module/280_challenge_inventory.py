from collections import Counter

inventory=Counter(apple=120,mangoes=30,lemons=100,strawberry=50)

order=Counter(mangoes=10,lemons=30,strawberry=5)

def update_inventory(inv,ord):
    inventory.subtract(ord) #both are type object of counter class
    print(inventory)

update_inventory(inventory,order)