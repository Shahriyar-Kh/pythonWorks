import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
cln=db.Customer

print("\n*************************** only 3 row retrive ******************** ")
x=cln.find().limit(3)
for i in x:
    print(i)

