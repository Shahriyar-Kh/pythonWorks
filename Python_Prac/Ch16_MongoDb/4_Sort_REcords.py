import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

#Access database
db=client.Sharydb

#Access collection
collection=db.Customer

print("\n***********************  Sorting in Ascending ****************")
records=collection.find().sort("name",1)

for i in records:
    print(i)
print("\n***********************  Sorting in Descending ****************")
records=collection.find().sort("Address",-1)

for i in records:
    print(i)