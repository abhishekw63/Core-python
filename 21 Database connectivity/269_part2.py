import pprint
import sqlite3
conn=sqlite3.Connection('shop.db')
cur=conn.cursor()

table=cur.execute('select * from Customers')
pprint.pprint(table)