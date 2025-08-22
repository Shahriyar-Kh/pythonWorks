from pymongo import MongoClient

myclient=MongoClient("mongodb://localhost:27017")

#Access database 
db=myclient.Sharydb

#Access collection
collection=db.TutorialPoint
for i in collection.find():
    print(i)

print("\n\n************* $exist using ******************")
x=collection.find({"City":{"$exists":True}})

for docs in x:
    print(i)

print("\n\n************* $exist and type using ******************")
x=collection.find({"_id":{"$exists":True,"$type":7}})
for docs in x:
    print(i)