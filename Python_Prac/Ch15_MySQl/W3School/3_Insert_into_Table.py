import mysql.connector
#Create connections
conn=mysql.connector.connect(
    host="localhost",
    user="Shahriyar",
    password="shary786",
    db='mydatabase'

)
print("\n********************  Checking Connection ******************************")
if conn.is_connected:
    print("Connection is Done!")
else:
    print("Wrong Connection")

cr=conn.cursor()
print("\n************************* Insert single row into table  *************************")
cr.execute("""Insert into Customer_tb (cust_name,cust_address,cust_Post) 
           values ("Shary","Charsadda","HR")
           """)
#Save the record
#Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
conn.commit()

#get the row id for inserted record
print("Id:",cr.lastrowid)
#print the number of records inserted
print(cr.rowcount,"Record inserted")


print("\n************************* Insert multiple row into table  *************************")
cr.execute("""Insert into Customer_tb (cust_name,cust_address,cust_Post) 
           values ("Shary","Peshawer","MR"),
                  ("Umair","Charsadda","GR"),
                  ("Hamad","Charsadda","HR"),
                  ("Ali","Mardan","     SR")
           """)
#Save the record
conn.commit()

#get the row id for inserted record
print("Id:",cr.lastrowid)
#print the number of records inserted
print(cr.rowcount,"Record inserted")