import pymongo

#create connection
client=pymongo.MongoClient("mongodb://localhost:27017/")

#Create database
db=client["Sharydb"]

#Create collection
collection=db["Customer"]
 
#insert one doc
dict={"name":"Shary","Address":"Charsadda","Marks":400}
collection.insert_one(dict)

#Drop database
client.drop_database('Shary')

print("\n************** Check databases **************")
#check data base 
dblist=client.list_database_names()
if "Sharydb" in dblist:
    print("The Sharydb is exist")

print("\n************** Rename databases **************")
old_db=client["mydb"]

client.admin.command("renameCollection",old_db, to="new_db")
print("\n************** Check collection **************")
clist=db.list_collection_names()
print(clist)
#Or check by name
if 'Customer' in clist:
    print("Customer is exist")




