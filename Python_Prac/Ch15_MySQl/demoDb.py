import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    password="shary786",
    user='Shahriyar',
    database="mydatabase"
)

if conn.is_connected():
    print("Conection done")
#Creating database name mydatabase

mycursor=conn.cursor()
try:
  mycursor.execute("CREATE DATABASE mydatabase")
except:
   print("Already created database")
   
#Check database exist
mycursor.execute("SHOW DATABASES")
for dbs in mycursor:
    print(dbs)
