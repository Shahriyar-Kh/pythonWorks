#Example  Limit the Results
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

print("\n\n********************** Limit Result 4 rows  *********************\n")
cr.execute("Select * from Customer_tb limit 4")

rows=cr.fetchall()
print("Cust_Id\t\tCust_name\tCust_Address\t\tCust_Post")
print("------------------------------------------------------------")
for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
print("\n\n********************** Limit Result 5 rows after 3 rows  *********************\n")
cr.execute("Select * from Customer_tb limit 5 offset 3")

rows=cr.fetchall()
print("Cust_Id\t\tCust_name\tCust_Address\t\tCust_Post")
print("------------------------------------------------------------")
for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
