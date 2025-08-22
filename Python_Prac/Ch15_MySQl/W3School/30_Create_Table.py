import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    password="shary786",
    user='Shahriyar',
    database="mydatabase"
)

if conn.is_connected():
    print("Conection done")
cr=conn.cursor()

try:
    cr.execute("create table Student (name varchar(255),RegNo int primary key,Class varchar(255),address varchar(255))")
    print("Student table is Created successfully")

except:
    print("Table is already exist")


cr.execute("show tables")
for tb in cr:
    print(tb)


# Primary Key
"""
When creating a table, you should also create a column with a unique key for each record.
This can be done by defining a PRIMARY KEY.
We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each recor"""

#Example  Create primary key when creating the table
try:
    cr.execute("Create table customer(id int auto_increment primary key,name varchar(255),address varchar(255))")
    print("Customer table is successfully created!")
except:
    print("customer table is already exist")


#Example Create primary key on an existing table:

    # cr.execute("Alter table Student add column RegNo int auto_increment primary key")
    # print("Update the column")
    # print("Already have primary key")

#Insert into table 

    sql="insert into customer (name,address) values (%s,%s)"
    val=("Shary","Charsadda")
    cr.execute(sql,val)
    # cr.commit()
    print(cr.rowcount,"Record inserted.")
    #Insert one row, and return the ID:
    print("1 record inserted, Id:",cr.lastrowid)

# Example Insert Multiple Rows
"""
To insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:"""


sql="insert into Student (RegNo,name,Class,address) values(%s,%s,%s,%s)"
val=[
    (18247,"Shary","BSSE","Charsadda"),
    (18248,"Hamad","BSSC","Charsadda 2"),
    (18249,"Ali","MLT","Peshawer"),
    (18250,"Yasir","DIT","Swaat"),
    (18251,"Umair","FSC","Mardan"),
    (18252,"Fahad","MS","Karachi")
]
cr.executemany(sql,val)
# cr.commit()
print(cr.rowcount,"Inserted data")

#Fetch the table 
cr.execute("select*from Student")
table=cr.fetchall()

print("Name\tRegNo\tClass\tAddress")
print("-------------------------------")
for row in table:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

#Selecting Columns
"""
To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):"""
cr.execute("select name,address from Student")
columns=cr.fetchall()
for c in columns:
    print(c)

#Using the fetchone() Method
"""
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:"""
cr.execute("Select * From Student")
row=cr.fetchone()
print("First row",row)
