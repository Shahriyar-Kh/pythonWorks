import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
cln=db.Customer

print("\n*************************** Delete_one() one row ******************** ")
q={"Address":"Charsadda"}
x=cln.delete_one(q)
print(x.deleted_count,"Document deleted.")

print("\n*************************** Delete_many() Multiple row ******************** ")
q={"Address":"Charsadda"}
x=cln.delete_many(q)

print(x.deleted_count,"Document deleted.")

print("\n*************************** Delete_many() Multiple row ******************** ")
x=cln.delete_many({})

print(x.deleted_count,"Document deleted.")

print("\n*************************** Drop Collection ******************** ")
cln.drop()
print("Collection dropes successfully")
