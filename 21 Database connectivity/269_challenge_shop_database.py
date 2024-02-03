import sqlite3

# Create a connection to the database
conn = sqlite3.connect('shop.db')

# Create a cursor object
c = conn.cursor()

"""# Create the Customer table
c.execute('''CREATE TABLE Customer (
    Custid INTEGER PRIMARY KEY,
    Cname TEXT NOT NULL,
    Address TEXT NOT NULL
)''')

# Create the Order table
c.execute('''CREATE TABLE Orders (
    OrderNo INTEGER PRIMARY KEY,
    Custid INTEGER NOT NULL,
    ProdNo INTEGER NOT NULL,
    Qty INTEGER NOT NULL,
    FOREIGN KEY (Custid) REFERENCES Customer(Custid),
    FOREIGN KEY (ProdNo) REFERENCES Product(ProdNo)
)''')

# Create the Product table
c.execute('''CREATE TABLE Product (
    ProdNo INTEGER PRIMARY KEY,
    Pname TEXT NOT NULL,
    Price REAL NOT NULL
)''')

# Insert data into the Customer table
c.execute("INSERT INTO Customer (Custid, Cname, Address) VALUES (101, 'Anita', 'Delhi')")
c.execute("INSERT INTO Customer (Custid, Cname, Address) VALUES (102, 'Raj', 'Hyderabad')")
c.execute("INSERT INTO Customer (Custid, Cname, Address) VALUES (103, 'Michael', 'Kolkata')")
c.execute("INSERT INTO Customer (Custid, Cname, Address) VALUES (107, 'All', 'Delhi')")
c.execute("INSERT INTO Customer (Custid, Cname, Address) VALUES (109, 'Sharma', 'Chennai')")

# Insert data into the Order table
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10005, 101, 10, 1)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10006, 101, 11, 2)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10007, 102, 12, 1)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10008, 103, 14, 1)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10009, 107, 11, 2)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10010, 103, 13, 4)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10011, 103, 10, 1)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10012, 103, 11, 4)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10013, 101, 12, 2)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10014, 101, 13, 1)")
c.execute("INSERT INTO Orders (OrderNo, Custid, ProdNo, Qty) VALUES (10015, 102, 14, 1)")

# Insert data into the Product table
c.execute("INSERT INTO Product (ProdNo, Pname, Price) VALUES (10, 'Toothpaste', 20)")
c.execute("INSERT INTO Product (ProdNo, Pname, Price) VALUES (11, 'Toothbrush', 10)")
c.execute("INSERT INTO Product (ProdNo, Pname, Price) VALUES (12, 'Lotion', 30)")
c.execute("INSERT INTO Product (ProdNo, Pname, Price) VALUES (13, 'Shampoo', 25)")
c.execute("INSERT INTO Product (ProdNo, Pname, Price) VALUES (14, 'Soap', 10)")"""

table=c.execute('pragma foreign_key="ON"')

for t in table:
    print(t)
# Commit the changes
conn.commit()

# Close the connection
conn.close()
