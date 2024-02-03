import sqlite3
conn = sqlite3.connect('shop.db')
c = conn.cursor()
'''
->find all customers :select * from Customer
->Find all customers from delhi:select * from Customer where Address="Delhi"
->Find all products with price greater than 20:select * from Product where Price>20
->find the names of products starting with letter 'S' :select * from Product where Pname like "S%" 
->find names of customers either living in Delhi or Chennai:select * from Customer where Address in("Delhi","Chennai")
->Find order no and product number with quantity greater than 1:select OrderNo,ProdNo from Orders where Qty>2
->find the name of customer with order number 10005: select Cname from Customer where Custid =(select Custid from Orders where OrderNo=10005)
->Find Product name and quantity in order number 63017:#mismatch in db: ->
    select p.Pname,o.Qty from Product p,Orders o,
    where o.ProdNo=p.Prodno and o.OrderNo=63017
->find order numbers which contains toothpaste:select Orders.OrderNo from Orders,Product where Orders.ProdNo=Product.ProdNo and Product.Pname="Toothpaste"
->find names of the customers who purchased lotion:
    'select c.Cname from Customer as c, Orders as o,Product as p
        where c.Custid=o.Custid and
        p.ProdNo=o.ProdNo and 
        p.Pname="Lotion"
'''
table=c.execute('''select c.Cname from Customer as c, Orders as o,Product as p
                where c.Custid=o.Custid and p.ProdNo=o.ProdNo and p.Pname="Lotion"''')

for t in table:
    print(t)
    
    
conn.commit()
conn.close()