from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017")

# Access database 
db = myclient.Sharydb

# Access collection
collection = db.TutorialPoint

# Print all documents in the collection
print("All documents in the collection:")
for doc in collection.find():
    print(doc)

print("\n************* using $regex to find ************")
# Use $regex to find documents where the 'Name' field starts with 'P'

for doc in collection.find({"Name": {"$regex": "^S"}}):
    print(doc)

print("\n************* using $text to find ************")
# #Create text index
# idx=collection.create_index({"Bio":"text"})

# for doc in collection.find({"$text":{"$search":"youtube"}}):
#     print(doc)

print("\n************* using $mod to find ************")

for doc in collection.find({"Age":{"$mod":[2,0]}}):
    print(doc)
