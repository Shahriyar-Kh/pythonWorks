#Example  Delete records
"""Sort the result alphabetically by name: result:"""
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="Shahriyar",
    password="shary786",
    database="mydatabase"
)
print("\n********************* Check Connection *******************")
if conn.is_connected:
    print("Connection done")
else:
    print("Wrong connection ")

cr=conn.cursor()

print("\n\n********************** Delete Records  *********************\n")
cr.execute("Delete from Customer_tb where Cust_address='Peshawer'")

print(cr.rowcount,"Record(s) Deleted")

print("\n\n********************** Delete Records using Escap char  *********************\n")
sql=("Delete from Customer_tb where Cust_address=%s")
adr=("Charsadda",)
cr.execute(sql,adr)

print(cr.rowcount,"Record(s) Deleted")
