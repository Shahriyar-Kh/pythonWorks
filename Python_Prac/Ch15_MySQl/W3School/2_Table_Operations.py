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


print("\n************************* Create Table  *************************")

#create cursor class instance
cr=conn.cursor()

#Create table with fields

tb=(""" Create table if not exists Customer_tb( 
           cust_id int not null auto_increment,
           cust_name varchar(255) not null,
           cust_address varchar(255),
           Cust_Post varchar(255),
           primary key(cust_id))
           """)
#Execute Sql query using Execute method
cr.execute(tb)
print("Customer_tb is created")

cr.execute("Create table if not exists sharytb(id int)")

print("\n********************** Show tables ***************************")
cr.execute("show tables")
for tbs in cr:
    print("Tables:\n",tbs)

print("\n*********************    Drop tables  *****************************")
try:
    cr.execute("Drop table sharytb")
    print("sharytb is droped")
except:
    print("sharytb is not exist")
print("\n***********************  Alter table  ******************************")
print("\n*********** Add column *************")

# Add cust_salary column
cr.execute("Alter table Customer_tb add cust_salary varchar(255)")
print("Added the Cust_salary column" )

print("\n*********** modify column *************")
# cr.execute("ALTER TABLE Customer_tb drop column cust_name")
# print("Droped column cust_salary")

print("\n********************* *****************************")

