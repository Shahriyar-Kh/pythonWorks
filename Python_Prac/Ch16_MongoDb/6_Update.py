import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
cln=db.Customer

print("\n*************************** Update_one() one row ******************** ")
old_q={"Address":"Charsadda"}
new_q={"$set":{"Address":"Karachi"}}

print("\n*************************** Update_one() one row ******************** ")
old_q={"Address":"Charsadda"}
new_q={"$set":{"Address":"Karachi"}}
x=cln.update_one(old_q,new_q)

for rows in cln.find():
    print(rows)

print("\n*************************** Update_many() one row ******************** ")
old_q={"Address":{"$regex":"Islamabad"}}
new_q={"$set":{"Address":"Peshawer"}}

x=cln.update_many(old_q,new_q)

for rows in cln.find():
    print(rows)