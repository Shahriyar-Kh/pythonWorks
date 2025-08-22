import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    password="shary786",
    user='Shahriyar'
)
print("\n******************** Check Connection *****************************")
if conn.is_connected():
    print("Conection done")
else:
    print("Not connection")


print("\n********************** Creating Database *****************************")
#Creating a Database  use the "CREATE DATABASE" statement
cr=conn.cursor()
#db name
db_name="mydatabase"
try:
    cr.execute("CREATE DATABASE {}".format(db_name))
    print("Database {} created ".format(db_name))
except:
    print(f"{db_name} already exists")



print("\n************************* Show Database *****************************")
cr.execute("Show databases")

for dbs in cr:
    print(dbs)

print("\n************************* Database Version *********************************")

cr.execute("select version()")
for ver in cr:
    print("Version available",ver)




print("\n************************* Drop Database ************************")
#Example Drop database (Drop database dbname)
db_name1='my_database'
try:
    cr.execute(f"Drop database {db_name1}")
    print(f"Droped {db_name1}")
except:
    print(f"{db_name1} not exists")

print("\n************************* Rename Database ************************")
# old_db='mydatabase'
# new_db="Sharydb"
# # try:
# cr.execute("ALTER DATABASE {} RENAME TO {}".format(db_name, new_db))
# print(f"{db_name} Ranme to {new_db}")
# except:
#     print("Already Renamed ")