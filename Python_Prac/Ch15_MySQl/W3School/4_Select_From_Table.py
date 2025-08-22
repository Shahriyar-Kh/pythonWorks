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
print("\n************************* Select from table   *************************")

print("\n********************* Fetchall()   ********************")
cr.execute("Select * from Customer_tb")

rows=cr.fetchall()
print("Cust_Id\t\tCust_name\tCust_Address\t\tCust_Post")
print("------------------------------------------------------------")
for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

print("\n********************* Fetchone()   ********************")
# cr.execute("Select * from Customer_tb ")
# row=cr.fetchone()
# print(row)

print("\n********************* Select with filter    ********************")
print("\n********** Where cluase    ********")

cr.execute("""SELECT * FROM Customer_tb WHERE cust_name = 'Shary'""")
result = cr.fetchall()
for row in result:
    print(row)

print("\n************ Wildcard char **********")
cr.execute("""SELECT * FROM Customer_tb WHERE Cust_address like '%adda%'""")
result = cr.fetchall()
for row in result:
    print(row)

print("\n************ %s Escap char **********")
sql="Select * from Customer_tb where Cust_address=%s"
adr=("Peshawer",)
cr.execute(sql,adr)

result=cr.fetchall()
for rows in result:
    print(rows)