#Example  Update table
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

print("\n\n********************** Update Records  *********************\n")

cr.execute("Update Customer_tb set Cust_address='Swaat' where Cust_address='Charsadda'")

print(cr.rowcount,"Record(s) Updated")

cr.execute("Select * from Customer_tb")

rows=cr.fetchall()
print("Cust_Id\t\tCust_name\tCust_Address\t\tCust_Post")
print("------------------------------------------------------------")
for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")