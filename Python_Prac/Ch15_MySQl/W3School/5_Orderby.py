#Example  orderby
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

print("\n\n**********************  Order by *********************\n")
cr.execute("Select * from Customer_tb order by Cust_name")
result=cr.fetchall()

print("Cust_ID\t Cust_name\t Cust_Address\t Cust_Post")
print("-------------------------------------------------------")
for rows in result:
    print(f"{rows[0]}\t{rows[1]}\t\t{rows[2]}\t{rows[3]}")

print("\n\n**********************  Order by desc *********************\n")
cr.execute("Select * from Customer_tb order by Cust_name desc")
result=cr.fetchall()

print("Cust_ID\t Cust_name\t Cust_Address\t Cust_Post")
print("-------------------------------------------------------")
for rows in result:
    print(f"{rows[0]}\t{rows[1]}\t\t{rows[2]}\t{rows[3]}")
    