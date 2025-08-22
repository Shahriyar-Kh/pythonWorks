import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")


#Access database
db=client.Sharydb

#Create Colection
collection=db["TutorialPoint"]

print("\n************* Find array element *****************")
for doc in collection.find({"experienc.Company":"Google"}):
    print(doc)

print("\n************* Find array element *****************")
for doc in collection.find({"experienc":{"$size":2}}):
    print(doc)

print("\n************* Find array element *****************")
for doc in collection.find({"experienc":{"$all":{"Amazon","Google"}}}):
    print(doc)